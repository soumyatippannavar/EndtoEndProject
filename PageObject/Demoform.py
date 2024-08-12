import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Pagedemo:

    #captch = "//div[@class='recaptcha-checkbox-border']"
    full_name = "Name"
    email ="Email"
    #company_id ="Form_getForm_CompanyName"
    phone= "Contact"
    country_css="select#Form_getForm_Country"

    def __init__(self,driver):
        self.driver = driver

    def enterformdetails(self,name,email,phone):
        self.driver.find_element(By.NAME,self.full_name).send_keys(name)
        time.sleep(1)
        self.driver.find_element(By.NAME,self.email).send_keys(email)
        time.sleep(1)
        self.driver.find_element(By.NAME, self.phone).send_keys(phone)
        time.sleep(1)
        #self.driver.find_element(By.XPATH,self.captch).click()
        self.driver.refresh()
        time.sleep(3)

    def countrydropdown(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.country_css)