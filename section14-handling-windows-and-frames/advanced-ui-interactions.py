import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# Create service object which will interact with chrome browser
# Service obj will use the chromedriver from the specified path to invoke chrome browser
service_obj = Service("../resources/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# define max wait time for locating elements.
# For example, implicit wait is 5 seconds, element located in 2 seconds
# then it will not wait anymore (save 3 seconds).
# important note: implicit wait not applicable for find_elements(), if elements not located returns [] - doesn't wait implicitly

driver.implicitly_wait(5)  # 5 seconds

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
time.sleep(2)
driver.close()

