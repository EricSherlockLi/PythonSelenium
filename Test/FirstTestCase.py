# Test Case
# 1. Open Web Browser(Chrome/Edge/Firefox)
# 2. Open URL
# 3. Enter username
# 4. Enter password
# 5. Click on Login
# 6. Capture title of the home page
# 7. Verify title of the page: OrangeHRM
# 8. Close browser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path=r"C:\Users\hello\PythonSelenium\Test\webdriver\chromedriver.exe", options=chrome_options)
