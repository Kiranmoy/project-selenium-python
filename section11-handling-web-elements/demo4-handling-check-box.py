import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Create service object which will interact with chrome browser
# Service obj will use the chromedriver from the specified path to invoke chrome browser
service_obj = Service("../resources/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        time.sleep(2)   # 2 seconds
        print(checkbox.is_selected())
        break
