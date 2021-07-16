'''Importing required modules'''
import json
from datetime import date
from database import Database
from config_operations import Config
from validation import Validation
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)
class App:
    '''App Class'''
    def __init__(self):
        self.fir_name = None
        self.mid_name = None
        self.las_name = None
        self.dob = None
        self.gender = None
        self.nat = None
        self.city = None
        self.state = None
        self.pin = None
        self.qual = None
        self.salary = None
        self.pan = None
        self.curdate = None
    def get_input(self):
        '''To get Inputs'''
        logger.debug("Getting Inputs")
        self.fir_name = input('Enter First Name:- ')
        self.mid_name = input('Enter Mid Name:- ')
        if not self.mid_name:
            self.mid_name = None
        self.las_name = input('Enter Last Name:- ')
        year, mon, dat = map(int, input('Enter DOB(0000-00-00):- ').split('-'))
        self.dob = date(year, mon, dat)
        self.gender = input('Enter Gender (\'M\' or \'F\'):- ')
        self.nat = input('Enter Nationality:- ')
        self.city = input('Enter Your City:- ')
        self.state = input('Enter Your State:- ')
        self.pin = input('Enter Pin code:- ')
        self.qual = input('Enter your qualification:- ')
        self.salary = float(input('Enter your salary:- '))
        self.pan = input('Enter your pan number:- ')
        self.curdate = date.today()
    def operations(self):
        '''Implementing the operations'''
        logger.debug("Get started with doing operations")
        config_obj = Config()
        data = {'host': "localhost", 'user': "root", 'password': ""}
        config_obj.config_file_write('config.ini', 'mysql', data)
        data_base = Database(auth_detail=config_obj.config_file_read('config.ini', 'mysql'))
        data_base.create_database('newdb')
        data_base.show_database()
        data_base.connect_database('newdb')
        data_base.create_table('usereq', 'id int NOT NULL AUTO_INCREMENT,'
                                         ' FIRSTNAME VARCHAR(20) NOT NULL,' \
                   ' MIDNAME VARCHAR(20), LASTNAME VARCHAR(20) NOT NULL, DOB DATE' \
                   ' NOT NULL, GENDER VARCHAR(5) NOT NULL, NATIONALITY VARCHAR(20)' \
                   ' NOT NULL, CITY VARCHAR(20) NOT NULL, STATE VARCHAR(20) NOT NULL,' \
                   ' PIN VARCHAR(7) NOT NULL, QUALIFICATION VARCHAR(20) NOT NULL,' \
                   ' SALARY FLOAT(8) NOT NULL, CURDATE DATE NOT NULL, PAN VARCHAR(10)' \
                   ' NOT NULL, PRIMARY KEY (id)')
        data_base.insert_table('usereq', '(FIRSTNAME, MIDNAME, LASTNAME,'
                                         ' DOB, GENDER, NATIONALITY,' \
                   ' CITY, STATE, PIN, QUALIFICATION, SALARY, PAN, curdate)',
                               '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                               (self.fir_name, self.mid_name, self.las_name, self.dob,
                  self.gender, self.nat, self.city, self.state, self.pin,
                  self.qual, self.salary, self.pan, self.curdate))
        data_base.create_table('useres', 'id int NOT NULL AUTO_INCREMENT, req_id int,' \
                   ' response blob, FOREIGN KEY (req_id) references' \
                   ' usereq(id), PRIMARY KEY (id)')
        for value in data_base.select_rows('usereq', '*', 'id not in '
                                                   '(select req_id from useres)'):
            res = {'Response': None}
            vald = Validation(req_id=value[0], dob=value[4], gender=value[5], pan=value[13],
                              req_date=value[12], nat=value[6], state=value[8], salary=value[11])
            if not (vald.date_format_checker() or vald.age_checker()
                    or vald.request_interval_checker()
                    or vald.nat_checker() or vald.state_checker()
                    or vald.salary_checker()):
                res['Response'] = 'Success'
            else:
                if vald.date_format_checker():
                    res['Response'] = 'Validation failure'
                    res['Reason'] = vald.date_format_checker()
                elif vald.age_checker() or\
                        vald.request_interval_checker()\
                        or vald.nat_checker() or vald.state_checker()\
                        or vald.salary_checker():
                    lis = [vald.age_checker(),
                           vald.request_interval_checker(),
                           vald.nat_checker(), vald.state_checker(),
                           vald.salary_checker()]
                    res['Response'] = 'Failed'
                    res['Reason'] = list(filter(lambda val: val is not None, lis))
            data_base.insert_table('useres', '(req_id, response)', '(%s, %s)',
                                   (value[0], json.dumps(res)))
        data_base.close()
app = App()
app.get_input()
app.operations()
