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
    company = "//a[text()='Company']"
    solution= "//ul//li[1]//a[text()='Solutions']"
    whyorange="//ul//li[2]//a[text()='Why OrangeHRM']"
    resource= "//ul//li[3]//a[text()='Resources']"
    about="//ul//li[4]//a[text()='About Us']"
    about_list="//ul//li[4]/div[@class='secondary secondary-menu-4']//ul//li"

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

    def aboutmenubar(self):
        return self.driver.find_element(By.XPATH,self.company)

    def aboutsunmenu(self):
        self.driver.find_element(By.XPATH,self.about).click()

    def solutionmenubar(self):
        return self.driver.find_element(By.XPATH,self.solution)

    def myorangemenubar(self):
        return self.driver.find_element(By.XPATH, self.whyorange)

    def resourcemenubar(self):
        return self.driver.find_element(By.XPATH, self.resource)