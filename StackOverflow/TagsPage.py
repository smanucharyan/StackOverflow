import pytest
import os
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TagsPage():

    page_title = {"by": By.CSS_SELECTOR, "value": "#mainbar-full > h1"}
    page_description = {"by": By.CSS_SELECTOR, "value": "#mainbar-full > p"}
    show_all_tags_syn_button = {"by": By.CSS_SELECTOR, "value": "#mainbar-full > div.grid.fw-wrap.gs4.mb24.ai-center > a"}
    all_tags_result_text = {"by": By.CSS_SELECTOR, "value": "#content > div:nth-child(1) > h1"}
    javascript = {"by": By.CSS_SELECTOR, "value": "#tags-browser > div:nth-child(1) > div.grid.jc-space-between.ai-center.mb12 > div > a"}
    javascript_page_text = {"by": By.CSS_SELECTOR, "value": "#mainbar > div.grid > div.grid.fl1.mb24 > h1"}
    filter = {"by": By.ID, "value": "tagfilter"}
    python_result = {"by": By.CSS_SELECTOR, "value": "#tags-browser > div:nth-child(1) > div.grid.jc-space-between.ai-center.mb12 > div > a"}
    number_python_questions = {"by": By.CSS_SELECTOR, "value": "#tags-browser > div:nth-child(1) > div.mt-auto.grid.jc-space-between.fs-caption.fc-black-300 > div:nth-child(1)"}



    def __init__(self, DRIVER):
        self.DRIVER = DRIVER
        DRIVER.get("https://stackoverflow.com/tags")

    def show_page_title(self):
        return self.DRIVER.find_element(self.page_title["by"], self.page_title["value"]).is_displayed()

    def show_page_description(self):
        return self.DRIVER.find_element(self.page_description["by"], self.page_description["value"]).is_displayed()

    def go_to_all_tags_syn(self):
        self.DRIVER.find_element(self.show_all_tags_syn_button["by"], self.show_all_tags_syn_button["value"]).click()

    def show_all_tags_syn_text(self):
        return self.DRIVER.find_element(self.all_tags_result_text["by"], self.all_tags_result_text["value"]).is_displayed()

    def go_to_javascript(self):
        self.DRIVER.find_element(self.javascript["by"], self.javascript["value"]).click()

    def show_javascript_result(self):
        return self.DRIVER.find_element(self.javascript_page_text["by"], self.javascript_page_text["value"]).is_displayed()

    def go_to_filter(self):
        self.DRIVER.find_element(self.filter["by"], self.filter["value"]).click()

    def filter_text(self):
        inputElement = self.DRIVER.find_element_by_id("tagfilter")
        inputElement.send_keys('python')
        inputElement.send_keys(Keys.ENTER)

    def show_filter_result(self):
        return self.DRIVER.find_element(self.python_result["by"], self.python_result["value"]).is_displayed()

    def show_number_of_PyQuestions(self):
        return self.DRIVER.find_element(self.number_python_questions["by"], self.number_python_questions["value"]).is_displayed()