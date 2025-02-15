from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# FLOW: script >> chromedriver >> chrome browser

# Create service object which will interact with chrome browser
# Service obj will automatically download driver from web, since chromedriver path not provided
# Invoke chrome browser using the downloaded chromedriver
service_obj = Service()
driver = webdriver.Firefox(service=service_obj)
driver.get("https://google.com")
driver.close()

# Create service object which will interact with chrome browser
# Service obj will use the chromedriver from the specified path to invoke chrome browser
service_obj = Service("../resources/geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
print(driver.title)
print(driver.current_url)
driver.close()