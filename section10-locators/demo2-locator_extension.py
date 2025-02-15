from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Create service object which will interact with chrome browser
# Service obj will use the chromedriver from the specified path to invoke chrome browser
service_obj = Service("../resources/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client/")

full_linkText = driver.find_element(By.LINK_TEXT,"Forgot password?").text
print(full_linkText)

partial_linkText = driver.find_element(By.PARTIAL_LINK_TEXT,"Forgot").text
print(partial_linkText)

driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@email.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
driver.find_element(By.XPATH, "//button[text()='Save New Password']")

