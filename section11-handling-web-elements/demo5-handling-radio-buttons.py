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

radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[2].click()
time.sleep(2)   # 2 seconds
print(radiobuttons[2].is_selected())

print(driver.find_element(By.ID,"displayed-text").is_displayed())
driver.find_element(By.ID, "hide-textbox").click()
print(driver.find_element(By.ID,"displayed-text").is_displayed())