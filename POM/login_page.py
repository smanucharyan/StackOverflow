import pytest
import os
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from POM import secure_page

class LoginPage():
    username_input = {"by": By.ID, "value": "username"}
    password_input = {"by": By.ID, "value": "password"}
    login_button = {"by": By.CSS_SELECTOR, "value": "button"}
    success_message = {"by": By.CSS_SELECTOR, "value": ".flash.success"}

    def __init__(self, DRIVER):
        self.DRIVER = DRIVER
        DRIVER.get("http://the-internet.herokuapp.com/login")

    def login_(self, username, password):
        self.DRIVER.find_element(self.username_input["by"], self.username_input["value"]).send_keys(username)
        self.DRIVER.find_element(self.password_input["by"], self.password_input["value"]).send_keys(password)
        self.DRIVER.find_element(self.login_button["by"], self.login_button["value"]).click()
        return secure_page.SecurePage(self.DRIVER)

    def success_message_present(self):
        return self.DRIVER.get_element(self.success_message["by"], self.success_message["value"]).is_displayed()
