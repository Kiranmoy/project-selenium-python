import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("../resources/chromedriver.exe")

# ChromeOptions
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--start-maximized")                # start the browser in maximized mode
chrome_options.add_argument("headless")                         # headless execution configuration
chrome_options.add_argument("--ignore-certificate-errors")      # disable SSL certificate checks
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)  # 5 seconds

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice")

time.sleep(2)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("headless-mode-screenshot.png")

driver.close()
driver.quit()