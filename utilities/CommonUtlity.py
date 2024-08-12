import inspect

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import logging


@pytest.mark.usefixtures("setup")
class BaseClass:

    def username(self):
        return "admin@yourstore.com"

    def password(self):
        return "admin"

    def selectcls(self,index,webele):
        drop = Select(webele)
        drop.select_by_index(index)

    def screenshot(self):
        self.driver.execute_script("window.scrollBy(0,1500)","")
        self.driver.get_screenshot_as_file("C:/Users/EI12548/PycharmProjects/pythonProject/Webdriver/screenshots/page.png")

    def waitforele(self):
        self.driver.implicitly_wait(3)

    def movrtoele(self,ele):
        Actions = ActionChains(self.driver)
        Actions.move_to_element(ele).perform()
        Actions.click().perform()

    def loggingfun(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  #filehandler object

        logger.setLevel(logging.DEBUG)
    #logger.debug("A debug statement is executed")
    #logger.info("Information statement")
    #logger.debug("A debug statement is executed")
    #logger.warning("Something is in warning mode")
    #logger.error("A Major error has happend")
    #logger.critical("Critical issue")
        return logger