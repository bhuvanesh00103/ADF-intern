import mysql.connector
import configparser

def config_file_write():
    config = configparser.ConfigParser()
    config['mysql'] = {'host': "127.0.0.1",
                       'user': "root", 'password': "Password"}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def config_file_read():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return [config.get('mysql', key) for key in list(config['mysql'])]

class Database:
    def __init__(self, db):
        self.host = db[0]
        self.user = db[1]
        self.password = db[2]
    def show_database(self):
        mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )
        mycursor = mydb.cursor()
        mycursor.execute("SHOW DATABASES")
        for x in mycursor:
            print(x)
    def print(self):
        print(self.host, self.user, self.password)
db = Database(config_file_read())
db.show_database()