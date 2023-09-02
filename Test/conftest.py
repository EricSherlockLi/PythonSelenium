import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver():
    run_env = os.environ.get('RUN_ENV', 'local')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    if run_env == 'ci':
        executable_path = '/usr/bin/chromedriver'
    else:
        executable_path = r"C:\Users\hello\PythonSelenium\Test\utils\webdriver\chromedriver.exe"

    service = Service(executable_path=executable_path)
    driver = webdriver.Chrome(service=service, options=options)
    yield driver  # 提供测试用例使用的WebDriver实例
    driver.quit()  # 测试用例执行结束后，关闭浏览器窗口


