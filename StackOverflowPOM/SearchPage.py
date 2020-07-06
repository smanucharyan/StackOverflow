import pytest
import os
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class SearchPage():

    search_input = {"by": By.XPATH, "value": "/html/body/header/div/form/div/input"}
    search_result_text = {"by": By.CSS_SELECTOR, "value": "#mainbar > div.grid.ai-center.mb16 > div.grid--cell.fl1.fs-body3.mr12"}
    question1 = {"by": By.CSS_SELECTOR, "value": "#question-summary-42939454 > div.summary > div.result-link > h3 > a"}
    question2 = {"by": By.CSS_SELECTOR, "value": "#question-summary-26908049 > div.summary > div.result-link > h3 > a"}


    def __init__(self, DRIVER):
        self.DRIVER = DRIVER
        DRIVER.get("https://stackoverflow.com/")


    def go_to_search(self):
        self.DRIVER.find_element(self.search_input["by"], self.search_input["value"]).click()

    def input_text(self):
        inputElement = self.DRIVER.find_element_by_xpath("/html/body/header/div/form/div/input")
        inputElement.send_keys('.net core')
        inputElement.send_keys(Keys.ENTER)

    def show_search_result(self):
        return self.DRIVER.find_element(self.search_result_text["by"], self.search_result_text["value"]).is_displayed()

    def show_question1(self):
        return self.DRIVER.find_element(self.question1["by"], self.question1["value"]).is_displayed()

    def show_question2(self):
        return self.DRIVER.find_element(self.question2["by"], self.question2["value"]).is_displayed()




