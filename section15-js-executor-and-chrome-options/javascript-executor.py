import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("../resources/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)  # 5 seconds

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice")

time.sleep(2)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screenshot.png")

time.sleep(2)
driver.close()