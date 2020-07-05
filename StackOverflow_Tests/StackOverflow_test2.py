import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from StackOverflow import HomePage


class TestStack2():

    @pytest.fixture
    def driver (self, request):
        _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver')
        if os.path.isfile(_chromedriver):
            _service = Chrome(executable_path=_chromedriver)
            driver = webdriver.Chrome(service=_service)
        else:
            driver = webdriver.Chrome()

        def quit():
            driver.quit()

        request.addfinalizer(quit)
        return HomePage.HomePage(driver)


    def test_open_community(self, driver):
        time.sleep(2)
        driver.go_to_community()
        driver.show_all_questions()
        assert (driver.show_all_questions())