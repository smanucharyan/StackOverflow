import pytest
import os
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class BasePage():

    menu = {"by": By.XPATH, "value": "/html/body/header/div/div[1]/a[1]/span"}
    users = {"by": By.ID, "value": "nav-users"}
    users_page_text = {"by": By.XPATH, "value": "/html/body/div[4]/div[2]/div/h1"}
    homepage_button = {"by": By.XPATH, "value": "/html/body/header/div/div[1]/a[2]/span"}
    homepage_title = {"by": By.XPATH, "value": "/html/body/div[4]/div[2]/div[1]/h1"}
    products = {"by": By.XPATH, "value": "/html/body/headecr/div/ol[1]/li[1]/a"}
    customers = {"by": By.XPATH, "value": "/html/body/header/div/ol[1]/li[2]/a"}
    customers_text = {"by": By.XPATH, "value": "/html/body/div[3]/div[2]/div[3]/div/div[1]/h1"}
    use_cases = {"by": By.XPATH, "value": "/html/body/header/div/ol[1]/li[3]/a"}



    def __init__(self, DRIVER):
        self.DRIVER = DRIVER
        DRIVER.get("https://stackoverflow.com/")

    def go_to_menu (self):
        self.DRIVER.find_element(self.menu["by"], self.menu["value"]).click()

    def go_to_users(self):
        self.DRIVER.find_element(self.users["by"], self.users["value"]).click()

    def show_UsersPage_text(self):
        return self.DRIVER.find_element(self.users_page_text["by"], self.users_page_text["value"]).is_displayed()

    def go_to_HomePage(self):
        self.DRIVER.find_element(self.homepage_button["by"], self.homepage_button["value"]).click()

    def show_HomePage_title(self):
        return self.DRIVER.find_element(self.homepage_title["by"], self.homepage_title["value"]).is_displayed()

    def go_to_products(self):
        self.DRIVER.find_element(self.products["by"], self.products["value"]).click()

    def go_to_customers(self):
        self.DRIVER.find_element(self.customers["by"], self.customers["value"]).click()

    def show_Customers_text(self):
        return self.DRIVER.find_element(self.customers_text["by"], self.customers_text["value"]).is_displayed()

    def go_to_UseCases(self):
        self.DRIVER.find_element(self.use_cases["by"], self.use_cases["value"]).click()





