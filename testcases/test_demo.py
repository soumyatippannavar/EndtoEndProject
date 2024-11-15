import time
from PageObject.Demoform import Pagedemo
from utilities import readfromexcel
from utilities.CommonUtlity import BaseClass


class Test_demo_form(BaseClass):
    path = "C://Users//EI12548//PycharmProjects//pythonProject//Webdriver//utilities//logincredentials.xlsx"

    def test_demopage(self):
        self.dm = Pagedemo(self.driver)
        #self.Logger = self.loggingfun()
        #testself.Logger.info("***logged in with 3 credentials***")

        self.Rowcount = readfromexcel.getRow(self.path, "Sheet1")
        for r in range(2, self.Rowcount + 1):
            name = readfromexcel.readdata(self.path, "Sheet1", r, 1)
            email = readfromexcel.readdata(self.path, "Sheet1", r, 2)
            ph = readfromexcel.readdata(self.path, "Sheet1", r, 3)
            country = readfromexcel.readdata(self.path,"Sheet1", r, 4)

            self.dm.enterformdetails(name, email, ph)
            time.sleep(2)
            self.selectcls(country, self.dm.countrydropdown())
            time.sleep(1)
            self.dm.pagerefresh()
    #@pytest.mark.sanity
    def test_menubar(self):
        self.dm1 = Pagedemo(self.driver)
        self.movrtoele(self.dm1.solutionmenubar())
        time.sleep(2)
        self.movrtoele(self.dm1.myorangemenubar())
        time.sleep(2)
        self.movrtoele(self.dm1.resourcemenubar())
        time.sleep(2)
        self.movrtoele(self.dm1.aboutmenubar())
        time.sleep(2)
        self.dm1.aboutsunmenu()
        time.sleep(1)