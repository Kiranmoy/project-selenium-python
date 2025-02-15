import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("../resources/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)  # 5 seconds

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")

# switch to frame
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am able to automate frames")

# switch back to parent page
driver.switch_to.default_content()

print(driver.find_element(By.CSS_SELECTOR,"h3").text)

time.sleep(2)
driver.close()

