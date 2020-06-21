import pytest
import os
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class SecurePage():
    secure_title = {"by": By.CLASS_NAME, "value": "icon-lock"}
    text = {"by": By.CLASS_NAME, "value": "subheader"}
    logout = {"by": By.XPATH, "value": "//*[@id='content']/div/a/i"}
    success_message = {"by": By.CSS_SELECTOR, "value": ".flash.success"}

    def __init__(self, DRIVER):
        self.DRIVER = DRIVER
        DRIVER.get("https://the-internet.herokuapp.com/secure")


    def success_message_present(self):
        return self._is_displayed(self.success_message)

    def logout(self):
        self.click(self.logout)
        print("Log out")