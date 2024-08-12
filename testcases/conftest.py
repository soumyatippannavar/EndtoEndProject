import time
import undetected_chromedriver as webdriver
from selenium import webdriver
import pytest


#@pytest.fixture(scope="class")
@pytest.fixture()
def setup(request):

    global driver
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'edge':
        driver = webdriver.Edge()
    #url = "https://" + "admin@yourstore.com" + ":" + "admin" + "@" + "admin-demo.nopcommerce.com/login"

    #driver.get("https://admin-demo.nopcommerce.com/admin/")

    driver.get("https://www.orangehrm.com/en/30-day-free-trial")
    driver.maximize_window()
    time.sleep(6)

    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser",default="chrome")