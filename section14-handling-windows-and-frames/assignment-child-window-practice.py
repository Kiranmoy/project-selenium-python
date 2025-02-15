import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("../resources/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)  # 5 seconds

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR,".blinkingText").click()

# grab all open window handles
window_handles = driver.window_handles

# switch to the new window/tab
driver.switch_to.window(window_handles[1])
email = driver.find_element(By.XPATH,"//p[@class='im-para red']/strong/a").text.strip()
print(email)
time.sleep(2)
driver.close()

# switch back to parent window > Fill Username & Password and submit
driver.switch_to.window(window_handles[0])
driver.find_element(By.CSS_SELECTOR,"#username").send_keys(email)
driver.find_element(By.CSS_SELECTOR,"#password").send_keys(email)
driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()

error_alert = driver.find_element(By.XPATH,"//form[@id='login-form']/div[@style='display: block;']").text
print(error_alert)

assert error_alert == "Incorrect username/password."

time.sleep(2)
driver.close()

