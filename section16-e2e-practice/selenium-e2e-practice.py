import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("../resources/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)  # 5 seconds
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(2)

# //a[contains(@href,'shop')]   a[href*='shop']
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

# Add Blackberry Phone to Cart & Checkout
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
success_msg = driver.find_element(By.CSS_SELECTOR,".alert-success").text

print(success_msg)
assert "Success" in success_msg

time.sleep(2)
driver.close()