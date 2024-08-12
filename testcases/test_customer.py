import time

import pytest

from PageObject.CustomerPage import Customer
from PageObject.Loginpage import Login
from utilities.CommonUtlity import BaseClass
from utilities import readproperty
from ddt import ddt, data, unpack


@ddt
class Test_001_Customer(BaseClass):

    #@ddt(*readproperty.read_data("C:\\Users\\EI12548\\PycharmProjects\\pythonProject\\Webdriver\\Testdata\\new.xlsx", "Sheet1"))
    #@unpack
    def test_customer(self):
        self.lp = Login(self.driver)
        self.lp.setup_user(Test_001_Customer.username(self))
        self.lp.setup_password(Test_001_Customer.password(self))
        self.lp.click_on()
        #self.screenshot()
        time.sleep(2)
        self.cp = Customer(self.driver)
        #self.cp.customer_page("email", "password")
        self.cp.customer_page("uwuwja@gmail.com","nj1452#$")
        #Test_001_Customer.waitforele(2)
        time.sleep(2)
        self.screenshot()
        time.sleep(2)
        self.selectcls(1,self.cp.dropdown())
        time.sleep(3)
        self.cp.click()
        time.sleep(2)
        self.lp.loggedout()
        time.sleep(2)