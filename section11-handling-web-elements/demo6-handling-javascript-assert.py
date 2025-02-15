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

driver.find_element(By.CSS_SELECTOR, "#name").send_keys("KIRAN")
driver.find_element(By.ID, "alertbtn").click()

alert = driver.switch_to.alert
print(alert.text)

time.sleep(2)
alert.accept()
time.sleep(2)
# alert.dismiss()