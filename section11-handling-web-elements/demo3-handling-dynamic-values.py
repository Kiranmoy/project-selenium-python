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
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)   # 2 seconds

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == 'India':
        country.click()
        break

time.sleep(2)   # 2 seconds

print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))

# HANDLING DYNAMIC TEXT
# Note that .text works only for static values, any text value that is generated dynamically won't get returned.
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
