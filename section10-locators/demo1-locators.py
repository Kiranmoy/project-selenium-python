from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Create service object which will interact with chrome browser
# Service obj will use the chromedriver from the specified path to invoke chrome browser
service_obj = Service("../resources/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# SELECTORS: id, name, link text (full & partial), classname, xpath, css selector

driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()

# CSS SELECTOR SYNTAX: tagName[attribute='value'] -> input[type='submit']
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Kiranmoy Paul")

# XPATH SYNTAX: //tagName[@attribute='value'] -> //input[@type='submit']
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Successs" in message

# SelectorHub tool for validating custom XPATH & CSS SELECTOR
# index for multiple elements: (//input[@type='submit'])[3]
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello Again")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()

driver.close()





