import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from StackOverflow import BasePage


class TestStack1():

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
        return BasePage.BasePage(driver)


    def test_correct_text(self, driver):
        driver.go_to_menu()
        time.sleep(2)
        driver.go_to_users()
        driver.show_UsersPage_text()
        assert (driver.show_UsersPage_text())

    def test_nav_to_HomPage(self, driver):
        driver.go_to_HomePage()
        driver.show_HomePage_title()
        assert (driver.show_HomePage_title())

    def test_nav_to_Customers(self, driver):
        driver.go_to_customers()
        driver.show_Customers_text()
        assert (driver.show_Customers_text())

    def test_search_box(self, driver):
        driver.go_to_search()
        time.sleep(2)
        driver.input_text()
        time.sleep(2)
        driver.show_search_result()
        #time.sleep(2)
        assert (driver.show_search_result())