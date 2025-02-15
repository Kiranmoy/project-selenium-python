import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# Create service object which will interact with chrome browser
# Service obj will use the chromedriver from the specified path to invoke chrome browser
service_obj = Service("../resources/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# define max wait time for locating elements.
# For example, implicit wait is 5 seconds, element located in 2 seconds
# then it will not wait anymore (save 3 seconds).
# important note: implicit wait not applicable for find_elements(), if elements not located returns [] - doesn't wait implicitly

driver.implicitly_wait(5)  # 5 seconds

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

expected_list = ['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actual_list = []

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(products))
for product in products:
    # locator chaining - locating child elements from the parent elements
    actual_list.append(product.find_element(By.XPATH,"h4").text)
    product.find_element(By.XPATH,"div/button").click()

print(actual_list)
assert expected_list == actual_list

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# FUNCTIONAL VALIDATION
sum = 0
prices = driver.find_elements(By.CSS_SELECTOR,"td:nth-child(5) p")
total_amount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
for price in prices:
    sum = sum + int(price.text)
print(sum)
print(total_amount)
assert sum == total_amount


driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

discounted_amount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(discounted_amount)
assert discounted_amount < total_amount

driver.close()