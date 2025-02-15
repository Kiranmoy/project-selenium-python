import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("../resources/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)  # 5 seconds
driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(2)

print(driver.title)

time.sleep(2)
driver.close()
driver.quit()
