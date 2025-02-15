import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# STEP 1: Login into application and store the authentication cookie generated.
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.demo.guru99.com/test/cookie/selenium_aut.php")
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("abc123")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("123xyz")
driver.find_element(By.XPATH,"//button[@name='submit']").submit()

cookies = driver.get_cookies()
print(cookies)
driver.close()

# STEP 2: Used the stored cookie, to again login into application without using userid and password.

driver = webdriver.Chrome()
driver.maximize_window()

# Entering in to the domain first to use cookie
driver.get('http://demo.guru99.com/test/cookie/selenium_aut.php')
time.sleep(2)

for cookie in cookies:
    cookie['domain'] = "guru99.com"
    driver.add_cookie(cookie)

time.sleep(2)
driver.refresh()

login_text = driver.find_element(By.XPATH,"//center").text
if(login_text == "You are logged In"):
    print("Authenticated using stored cookie and logged in successfully")
driver.close()

driver.quit()



