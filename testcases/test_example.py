import time

import pytest
from selenium.webdriver.common.by import By

from PageObject.Catalog import Catalog
from PageObject.Loginpage import Login

from utilities.CommonUtlity import BaseClass


class Test_003_login(BaseClass):

    #@pytest.mark.sanity
    def test_new2(self):
        self.lp = Login(self.driver)
        self.lp.setup_user(Test_003_login.username(self))
        self.lp.setup_password(Test_003_login.password(self))
        self.lp.click_on()
        #self.lp.setup_user(param[0])
        #self.lp.setup_password(param[1])
        #self.lp.click_on()
        time.sleep(2)
        self.catalog = Catalog(self.driver)
        self.catalog.Catalog_page()
        self.catalog.Catalog_product("New prod2")
        time.sleep(5)
        self.catalog.save_product()
        time.sleep(5)
        self.catalog.search_product("New prod2")
        #self.driver.get_screenshot_as_file("searched_product.png")
        time.sleep(4)


#@pytest.fixture(params=[("admin@yourstore.com", "admin")])
#def param(request):
    #return request.param


