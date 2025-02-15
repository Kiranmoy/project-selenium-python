import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("../resources/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)  # 5 seconds
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# click on column header
# collect all veggie names -> BrowserSortedVeggieList (A, B, C)
# sort this BrowserSortedVeggieList -> newSortedList (A, B, C)
# BrowserSortedVeggieList (A, B, C) == newSortedList (A, B, C)
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggies_list= driver.find_elements(By.XPATH, "//tr/td[1]")
browser_sorted_veggies = []
for veggie in veggies_list:
    browser_sorted_veggies.append(veggie.text)

new_sorted_veggies = browser_sorted_veggies.copy()
new_sorted_veggies.sort()

print("BROWSER SORTED VEGGIES: ", browser_sorted_veggies)
print("MANUALLY SORTED VEGGIES: ", new_sorted_veggies)
assert  browser_sorted_veggies == new_sorted_veggies

time.sleep(2)
driver.close()



