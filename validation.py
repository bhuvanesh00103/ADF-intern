'''Importing required modules'''
from datetime import date
import datetime
from database import Database
from config_operations import Config

import logging

logging.basicConfig(filename='app.log',level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)
class Validation:
    '''To validate data'''
    def __init__(self, req_id, dob, gender, pan, req_date, nat, state, salary):
        logger.debug("Creating Validation Object")
        self.req_id = req_id
        self.dob = dob
        self.gender = gender
        self.pan = pan
        self.req_date = req_date
        self.nat = nat
        self.state = state
        self.salary = salary
    def date_format_checker(self):
        '''used check format of date'''
        logger.debug("Checking Format of Date of Birth")
        datetime.datetime.strptime(str(self.dob), '%Y-%m-%d')
        return None
    def age_checker(self):
        '''used to check age'''
        logger.debug("Checking Age")
        dob = self.dob
        current = date.today()
        age = int(str(current - dob)[:4]) / 365
        if not (age > 21 and self.gender.lower() == 'm')\
                or (age > 18 and self.gender.lower() == 'f'):
            return 'Age is less than expected'
        return None
    def request_interval_checker(self):
        '''used to check request interval'''
        logger.debug("Checking for request Interval")
        config_obj = Config()
        auth_detail = config_obj.config_file_read('config.ini', 'mysql')
        data_base = Database(auth_detail)
        data_base.connect_database('mydb')
        dates = data_base.select_rows('usereq', 'curdate',
                               f'id <> {self.req_id} and pan = \'{self.pan}\' and'
                               f' curdate <= \'{self.req_date}\'')
        data_base.close()
        for value in dates:
            diff = int(str(self.req_date - value[0])[:1])
            if diff < 5:
                return 'Recently request received in last 5 days'
        return None
    def nat_checker(self):
        '''used to check Nationality'''
        logger.debug("Checking Nationality")
        if self.nat.lower() not in ['indian', 'american']:
            return 'Indian and American are allowed'
        return None
    def state_checker(self):
        '''used to check state of the user'''
        logger.debug("Checking State")
        list_of_states = ['andhra pradesh', 'arunachal pradesh',
                          'assam', 'bihar',  'chhattisgarh',  'karnataka',
                          'madhya pradesh',  'odisha',  'tamilnadu',
                          'telangana', 'west bengal']
        if self.state.lower() not in list_of_states:
            return 'State was not expected one'
        return None
    def salary_checker(self):
        '''used to check salary range'''
        logger.debug("Salary Checker")
        if self.salary < 10000 or self.salary > 90000:
            return 'Salary should be expected range between 10000 and 90000'
        return None
