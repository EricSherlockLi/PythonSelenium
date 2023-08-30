# Test Case
# 1. Open Web Browser(Chrome/Edge/Firefox)
# 2. Open URL
# 3. Enter username
# 4. Enter password
# 5. Click on Login
# 6. Capture title of the home page
# 7. Verify title of the page: OrangeHRM
# 8. Close browser
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=r"C:\Users\hello\PythonSelenium\Test\webdriver\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
wait = WebDriverWait(driver, 10)

input_text = wait.until(EC.element_to_be_clickable(("name", "username")))
input_pwd = wait.until(EC.element_to_be_clickable(("name", "password")))
submit_button = wait.until(EC.element_to_be_clickable(("xpath", "//button[text()=' Login ']")))
# submit_button = driver.find_element("xpath", "//button[@type='submit']")

input_text.send_keys("Admin")
input_pwd.send_keys("admin123")
submit_button.click()
time.sleep(5)

home_page_title = driver.title

# 验证主页的标题
expected_title = "OrangeHRM"
if home_page_title == expected_title:
    print(f"Test successful: Home page title is {home_page_title}")
else:
    print(f"Test failed: Expected title {expected_title}, but got {home_page_title}")

# 关闭WebDriver实例
driver.quit()
