import pytest
import os
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class HomePage():

    for_developers={"by": By.XPATH, "value": "//*[@id='content']/div[1]/div/a[1]"}
    for_businesses = {"by": By.XPATH, "value": "//*[@id='content']/div[1]/div/a[2]"}
    open_community_button = {"by": By.XPATH, "value": "//*[@id='for-developers']/p/a"}
    all_questions_text = {"by": By.CSS_SELECTOR, "value": "#mainbar > div.grid > h1"}


    def __init__(self, DRIVER):
        self.DRIVER = DRIVER
        DRIVER.get("https://stackoverflow.com/")

    def go_to_ForDevelopers(self):
        self.DRIVER.find_element(self.for_developers["by"], self.for_developers["value"]).click()

    def go_to_ForBusinesses(self):
        self.DRIVER.find_element(self.for_businesses["by"], self.for_businesses["value"]).click()

    def go_to_community(self):
        self.DRIVER.find_element(self.open_community_button["by"], self.open_community_button["value"]).click()

    def show_all_questions(self):
        return self.DRIVER.find_element(self.all_questions_text["by"], self.all_questions_text["value"]).is_displayed()