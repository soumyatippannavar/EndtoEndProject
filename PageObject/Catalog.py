import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Catalog:

    catalog_button_xpath = "(//li[@class='nav-item has-treeview']/a/p)[1]"
    product_xpath = "//a[@href='/Admin/Product/List']"
    Add_user_xpath = "//a[@href='/Admin/Product/Create']"
    collapse_button = "//div[@id='product-info']"

    #"//div[@class='card card-default card-search']"

    product_name = "//input[@id='Name']"
    save_button = "//button[@name='save']"
    search_collapse_xpath = "// div[ @class ='icon-collapse']"
    search_product_textbox_id = "//input[@id='SearchProductName']"
    search_button = "search-products"


    def __init__(self, driver):
        self.driver = driver


    def Catalog_page(self):
        self.driver.find_element(By.XPATH, self.catalog_button_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.product_xpath).click()

    def Catalog_product(self, productname):
        self.driver.find_element(By.XPATH,self.Add_user_xpath).click()
        self.driver.find_element(By.XPATH, self.collapse_button).click()
        self.driver.find_element(By.XPATH,self.product_name).send_keys(productname)

    def save_product(self):
        self.driver.find_element(By.XPATH,self.save_button).click()

    def search_product(self, search_product):
        #self.driver.find_element(By.XPATH, self.search_collapse_xpath).click()
        self.driver.find_element(By.XPATH, self.search_product_textbox_id).send_keys(search_product)

        self.driver.find_element(By.ID, self.search_button).click()

