from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Create service object which will interact with chrome browser
# Service obj will use the chromedriver from the specified path to invoke chrome browser
service_obj = Service("../resources/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()

# CSS SELECTOR SYNTAX: tagName[attribute='value'] -> input[type='submit']
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Kiranmoy Paul")
driver.find_element(By.CSS_SELECTOR, "inlineRadio1").click()

# STATIC DROP DOWN HANDLING
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(0)
dropdown.select_by_value("Female")
dropdown.select_by_visible_text("Female")

# XPATH SYNTAX: //tagName[@attribute='value'] -> //input[@type='submit']
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
driver.close()
