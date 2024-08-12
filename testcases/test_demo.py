import time

from PageObject.Demoform import Pagedemo
from utilities import readfromexcel
from utilities.CommonUtlity import BaseClass


class Test_demo_form(BaseClass):
    path = "C://Users//EI12548//PycharmProjects//pythonProject//Webdriver//utilities//logincredentials.xlsx"

    def test_demopage(self):
        self.dm = Pagedemo(self.driver)
        self.Logger = self.loggingfun()
        self.Logger.info("***logged in with 3 credentials***")

        self.Rowcount = readfromexcel.getRow(self.path, "Sheet1")
        for r in range(2, self.Rowcount + 1):
            name = readfromexcel.readdata(self.path, "Sheet1", r, 1)
            email = readfromexcel.readdata(self.path, "Sheet1", r, 2)
            ph = readfromexcel.readdata(self.path, "Sheet1", r, 3)

            self.selectcls(1, self.dm.countrydropdown())
            time.sleep(2)
            self.dm.enterformdetails(name, email, ph)
            time.sleep(2)
