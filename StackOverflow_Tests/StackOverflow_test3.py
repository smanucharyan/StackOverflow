import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from StackOverflowPOM import TagsPage


class TestStack3():

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
        return TagsPage.TagsPage(driver)


    def test_page_title(self, driver):
        driver.show_page_title()
        assert (driver.show_page_title())

    def test_page_description(self, driver):
        driver.show_page_description()
        assert (driver.show_page_description())

    def test_all_tags_result_text(self, driver):
        time.sleep(2)
        driver.go_to_all_tags_syn()
        driver.show_all_tags_syn_text()
        assert (driver.show_all_tags_syn_text())

    def test_javascript_result(self, driver):
        driver.go_to_javascript()
        driver.show_javascript_result()
        assert (driver.show_javascript_result())


    def test_filter(self, driver):
        driver.go_to_filter()
        time.sleep(2)
        driver.filter_text()
        time.sleep(2)
        driver.show_filter_result()
        #time.sleep(2)
        assert (driver.show_filter_result())

    def test_number_of_questions(self, driver):
        driver.go_to_filter()
        time.sleep(2)
        driver.filter_text()
        time.sleep(2)
        driver.show_number_of_PyQuestions()
        # time.sleep(2)
        assert driver.show_number_of_PyQuestions()<1577558