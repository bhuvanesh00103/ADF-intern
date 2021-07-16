'''Importing required modules'''
import mysql.connector
from mysql.connector import errors
import logging

logging.basicConfig(filename='app.log',level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)
class Database:
    '''Database Class'''
    def __init__(self, auth_detail):
        logger.debug("Connecting to Localhost")
        try:
            self.mydb = mysql.connector.connect(
                host=auth_detail['host'],
                user=auth_detail['user'],
                password=auth_detail['password']
            )
            self.mycursor = self.mydb.cursor()
        except errors.ProgrammingError as err:
            logger.error("Failed to Connect LocalHost")
            print(err)
    def create_database(self, name):
        '''used to create database'''
        logger.debug("Trying create database")
        try:
            self.mycursor.execute("CREATE DATABASE " + name)
            logger.debug("Created Database....")
        except errors.DatabaseError as err:
            logger.error("Database Already Present")
            print(err)
    def show_database(self):
        '''used to show databases'''
        logger.debug("Showing the Databases present")
        self.mycursor.execute("SHOW DATABASES")
        for database in self.mycursor:
            print(database)
    def connect_database(self, db_name):
        '''used to connect to particular database'''
        logger.debug("Connecting to particular Database")
        self.mydb.database = db_name
        self.mycursor = self.mydb.cursor()
        logger.debug("Connected to database")
    def create_table(self, tb_name, entities):
        '''used to create tables'''
        try:
            logger.debug("Trying to create table")
            self.mycursor.execute("CREATE TABLE " + tb_name + "(" + entities + ")")
        except errors.ProgrammingError as err:
            logger.error("Table already Present")
            print(err)
    def show_tables(self):
        '''used to show tables in the database'''
        try:
            logger.debug("Showing Tables")
            self.mycursor.execute("SHOW TABLES")
            for table in self.mycursor:
                print(table)
        except errors.ProgrammingError as err:
            logger.error("Not connected to database")
            print(err)
    '''def desc_table(self, tb_name):
        try:
            self.mycursor.execute("DESC " + tb_name)
            for det in self.mycursor:
                print(det)
        except errors.ProgrammingError as err:
            print(err)'''
    def insert_table(self, tb_name, col_name, data_type, values):
        '''used to insert into table'''
        insert_stmt = (
            "INSERT INTO " + tb_name + " " + col_name +
            "VALUES " + data_type
        )
        logger.debug("Inserting to Table")
        self.mycursor.execute(insert_stmt, values)
    def select_rows(self, tb_name, column, condition = None):
        '''used to select rows from table'''
        logger.debug("Fetching Rows from the table")
        if not condition:
            self.mycursor.execute('SELECT '+ column +' from '+ tb_name)
        else:
            self.mycursor.execute('SELECT ' + column + ' from ' + tb_name + ' where ' + condition)
        return self.mycursor.fetchall()
    def close(self):
        '''Used to close Connection'''
        logger.debug("Closing the database connection")
        self.mydb.commit()
        self.mydb.close()
