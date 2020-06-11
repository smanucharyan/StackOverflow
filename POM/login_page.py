from selenium.webdriver.common.by import By

class LoginPage():
    username_input = {"by": By.ID, "value": "username"}
    password_input = {"by": By.ID, "value": "password"}
    login_button = {"by": By.CSS_SELECTOR, "value": "button"}
    success_message = {"by": By.CSS_SELECTOR, "value": ".flash.success"}

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("http://the-internet.herokuapp.com/login")

    def with_(self, username, password):
        self.driver.find_element(self.username_input["by"], self.username_input["value"]).send_keys(username)
        self.driver.find_element(self.password_input["by"], self.password_input["value"]).send_keys(password)
        self.driver.find_element(self.login_button["by"], self.login_button["value"]).click()

    def success_message_present(self):
        return self.driver.find_element(self.success_message["by"], self.success_message["value"]).is_displayed()
