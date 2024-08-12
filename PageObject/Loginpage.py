import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    text_user_id = "Email"
    text_password_id = "Password"
    click_button_xpath = "//*[@class='button-1 login-button']"
    error_text ="//span[text()='Please enter your email']"
    logout = "//*[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setup_user(self, user):
        self.driver.find_element(By.ID, self.text_user_id).clear()
        self.driver.find_element(By.ID, self.text_user_id).send_keys(user)

    def setup_password(self, password):
        self.driver.find_element(By.ID, self.text_password_id).clear()
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def clear_password_textbox(self):
        self.driver.find_element(By.ID, self.text_user_id).clear()
        self.driver.find_element(By.ID, self.text_password_id).clear()

    def click_on(self):
        self.driver.find_element(By.XPATH, self.click_button_xpath).click()

    def errormsg(self):
        errtext = self.driver.find_element(By.XPATH, self.error_text)
        print(errtext.text)

    def loggedout(self):
        self.driver.find_element(By.XPATH, self.logout).click()



    #def login_obj(self):
        #lp1 = Login(self.driver)
        #lp1.clear_password_textbox()
        #lp1.click_on()
        #time.sleep(2)