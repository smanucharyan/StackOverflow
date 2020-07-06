import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from StackOverflowPOM import SearchPage


class TestStack4():

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
        return SearchPage.SearchPage(driver)


    def test_search_box(self, driver):
        driver.go_to_search()
        time.sleep(2)
        driver.input_text()
        time.sleep(2)
        driver.show_search_result()
        #time.sleep(2)
        assert (driver.show_search_result())

    def test_search_question1(self, driver):
        driver.go_to_search()
        time.sleep(2)
        driver.input_text()
        time.sleep(2)
        driver.show_question1()
        #time.sleep(2)
        assert (driver.show_question1())

    def test_search_question2(self, driver):
        driver.go_to_search()
        time.sleep(2)
        driver.input_text()
        time.sleep(2)
        driver.show_question2()
        assert (driver.show_question2())