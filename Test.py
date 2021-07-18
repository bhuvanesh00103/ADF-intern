from datetime import date

import pytest

from validation import Validation


class Test:
    '''Test Class'''
    obj = Validation(1, date(1999, 3, 13), 'M', 'ASD1234567', '2021-07-05', 'Indian', 'TamilNadu', 50000)

    def test_date_format_checker1(self):
        ''''Method to test Date format'''
        assert  self.obj.date_format_checker() is None

    @pytest.mark.xfail
    def test_date_format_checker2(self):
        assert  self.obj.date_format_checker() == 'Failed to check'

    def test_age_checker1(self):
        assert self.obj.age_checker() is None

    @pytest.mark.xfail
    def test_age_checker2(self):
        assert self.obj.age_checker() == 'Age is less than expected'

    def test_request_interval_checker1(self):
        assert self.obj.request_interval_checker() is None

    @pytest.mark.xfail
    def test_request_interval_checker2(self):
        assert self.obj.request_interval_checker() == 'Recently request received in last 5 days'

    def test_nat_checker1(self):
        assert self.obj.nat_checker() is None

    @pytest.mark.xfail
    def test_nat_checker2(self):
        assert self.obj.nat_checker() == 'Indian and American are allowed'

    def test_state_checker1(self):
        assert self.obj.state_checker() is None

    @pytest.mark.xfail
    def test_state_checker2(self):
        assert self.obj.state_checker() == 'State was not expected one'

    def test_salary_checker1(self):
        assert self.obj.salary_checker() is None

    @pytest.mark.xfail
    def test_salary_checker2(self):
        assert self.obj.salary_checker() == 'Salary should be expected range between 10000 and 90000'
