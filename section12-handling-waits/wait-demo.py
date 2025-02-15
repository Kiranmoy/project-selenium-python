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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)   # 2 seconds
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(products))
for product in products:
    # locator chaining - locating child elements from the parent elements
    product.find_element(By.XPATH,"div/button").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
time.sleep(10)
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
time.sleep(2)

driver.close()