from Test.pages.login_page import LoginPage
import pytest
import sys
sys.path.append(r"C:\Users\hello\PythonSelenium")


@pytest.mark.login
def test_login(driver):
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    assert login_page.is_login_successful() is True, "Login failed with valid credentials."


@pytest.mark.login
def test_no_username(driver):
    login_page = LoginPage(driver)
    login_page.login("", "some_password")
    assert login_page.is_username_error_displayed() is True, "Username error box not displayed"


@pytest.mark.login
def test_no_password(driver):
    login_page = LoginPage(driver)
    login_page.login("some_username", "")
    assert login_page.is_password_error_displayed() is True, "Password error box not displayed"


@pytest.mark.login
def test_invalid_credentials_alert(driver):
    login_page = LoginPage(driver)
    login_page.login("wrong_username", "wrong_password")
    assert login_page.is_invalid_credentials_alert_displayed() is True, "Invalid credentials alert not displayed"
