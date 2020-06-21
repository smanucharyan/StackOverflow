import pytest
import os
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from POM import login_page
from POM import secure_page

class TestLogin():

    @pytest.fixture
    def DRIVER (self, request):
        _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver')
        if os.path.isfile(_chromedriver):
            _service = Chrome(executable_path=chromedriver)
            DRIVER = webdriver.Chrome(service=_service)
        else:
            DRIVER = webdriver.Chrome()

        def quit():
            DRIVER.quit()

        request.addfinalizer(quit)
        return login_page.LoginPage(DRIVER)

    def test_valid_credentials(self, DRIVER):
        DRIVER.login_("tomsmith", "SuperSecretPassword!")
        return secure_page.SecurePage(DRIVER)
        assert (login.success_message_present())

    def logout(self):
        logout.click()
        return login_page.LoginPage(DRIVER)
        assert (logout.success_message_present())




