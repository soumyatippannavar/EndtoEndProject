import time
import pytest
from PageObject.Loginpage import Login
from testcases.logging import Logs
from utilities.CommonUtlity import BaseClass
from utilities import readfromexcel


class Test_Datadriven(BaseClass):

    path = "C://Users//EI12548//PycharmProjects//pythonProject//Webdriver//utilities//logincredentials.xlsx"

    def test_logout(self):
        self.lp = Login(self.driver)
        #self.Logger = self.loggingfun()
        #self.Logger.info("******lodded in with 1st credentials")

        self.Rowcount = readfromexcel.getRow(self.path, "Sheet1")


        for r in range(2, self.Rowcount+1):
            username = readfromexcel.readdata(self.path,"Sheet1",r,1)
            password = readfromexcel.readdata(self.path, "Sheet1", r, 2)

            self.lp.setup_user(username)
            time.sleep(1)
            self.lp.setup_password(password)
            self.lp.click_on()
            time.sleep(2)
            self.lp.loggedout()
            time.sleep(2)