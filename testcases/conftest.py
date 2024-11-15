import time
#import undetected_chromedriver as webdriver
from selenium import webdriver
import pytest
from testcases import test_demo
from testcases.test_demo import Test_demo_form

@pytest.fixture(scope="class",autouse=True)
#@pytest.fixture(autouse=True)
def setup(request):

    global driver
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'edge':
        driver = webdriver.Edge()
    #driver.get("https://admin-demo.nopcommerce.com/admin/")
    driver.get("https://www.orangehrm.com/en/30-day-free-trial")
    driver.maximize_window()
    time.sleep(2)
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser",default="chrome")