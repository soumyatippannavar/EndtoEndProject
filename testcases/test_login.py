import logging
import time

import pytest

from PageObject.Loginpage import Login
from utilities.CommonUtlity import BaseClass

class Test_001_login(BaseClass):


    def test_verify_title(self):
        title = self.driver.title
        print(title)
        if title == 'Your store. Login':
            logger = self.loggingfun()
            logger.info(title)
            logger.debug(title)
            assert True
        else:
            time.sleep(3)
            #self.lp = Login(self.driver)
            self.screenshot()
            assert False


    def test_login_postive(self):
        self.lp = Login(self.driver)
        self.lp.setup_user(self.username())
        self.lp.setup_password(self.password())
        self.lp.click_on()
        time.sleep(2)
        self.lp.loggedout()
        time.sleep(2)


    #@pytest.mark.sanity
    def test_login_negative(self):
        self.lp1 = Login(self.driver)
        self.lp1.clear_password_textbox()
        self.lp1.click_on()
        self.screenshot()
        #Login.login_obj(self)
        time.sleep(2)
        #self.lp1.errormsg()