import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test.pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.LOGIN_URL)

    def enter_username(self, username):
        wait = WebDriverWait(self.driver, 10)
        input_username = wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD))
        input_username.send_keys(username)

    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 10)
        input_password = wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD))
        input_password.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

    def login(self, username, password):
        time.sleep(10)
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        time.sleep(5)

    def is_login_successful(self):
        dashboard_element = self.driver.find_element(By.CSS_SELECTOR,
                                                     "h6.oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module")
        return "Dashboard" in dashboard_element.text or "dashboard" in self.driver.current_url

    def is_username_error_displayed(self):
        error_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='username'].oxd-input--error")
        return error_input.is_displayed()

    def is_password_error_displayed(self):
        error_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='password'].oxd-input--error")
        return error_input.is_displayed()

    def is_invalid_credentials_alert_displayed(self):
        alert = self.driver.find_element(By.CSS_SELECTOR, "p.oxd-text.oxd-text--p")
        return alert.is_displayed()

