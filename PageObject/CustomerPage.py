import time
from selenium.webdriver.common.by import By


class Customer:

    customer_xpath= "(//li[@class='nav-item has-treeview']/a/p)[4]"
    customer_link= "//a[@href='/Admin/Customer/List']"
    add_new_cutomer= "//a[@href='/Admin/Customer/Create']"
    Email_id= "Email"
    password_id ="Password"
    Gender_mail_id="Gender_Male"
    customer_pageinfo="//div[@id='customer-info']"
    save_button = "//button[@name='save']"
    dropdown_id = "VendorId"

    def __init__(self, driver):
        self.driver = driver

    def customer_page(self, Email, password):

        self.driver.find_element(By.XPATH, self.customer_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.customer_link).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.add_new_cutomer).click()
        self.driver.find_element(By.XPATH, self.customer_pageinfo).click()
        time.sleep(2)
        self.driver.find_element(By.ID,self.Email_id).send_keys(Email)
        time.sleep(2)
        self.driver.find_element(By.ID, self.password_id).send_keys(password)
        self.driver.find_element(By.ID, self.Gender_mail_id).click()
        time.sleep(2)

    def dropdown(self):
        return self.driver.find_element(By.ID,self.dropdown_id)

    def click(self):
        self.driver.find_element(By.XPATH, self.save_button).click()