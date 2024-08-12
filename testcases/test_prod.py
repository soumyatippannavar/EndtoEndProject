import time

import pytest
from selenium.webdriver.common.by import By

from PageObject.Catalog import Catalog
from PageObject.Loginpage import Login
from utilities.CommonUtlity import BaseClass
class Test_product(BaseClass):

    def test_products(self):
        self.lp = Login(self.driver)
        self.lp.setup_user(Test_product.username(self))
        self.lp.setup_password(Test_product.password(self))
        self.lp.click_on()
        self.catalog = Catalog(self.driver)
        self.catalog.Catalog_page()
        self.catalog.Catalog_product("New prod2")
        time.sleep(5)
        self.catalog.save_product()
        time.sleep(5)
        self.catalog.search_product("New prod2")
        # self.driver.get_screenshot_as_file("searched_product.png")
        time.sleep(4)





