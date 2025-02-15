from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# FLOW: script >> chromedriver >> chrome browser

# Create service object which will interact with chrome browser
# Service obj will automatically download driver from web, since chromedriver path not provided
# Invoke chrome browser using the downloaded chromedriver

# service_obj = Service()
# driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()
driver.get("https://google.com")
driver.close()


# Create service object which will interact with chrome browser
# Service obj will use the chromedriver from the specified path to invoke chrome browser

service_obj = Service("../resources/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
print(driver.title)
print(driver.current_url)
driver.save_screenshot('screenshot.png')

# Gets the screenshot of the current window as a binary data.
image_bytes = driver.get_screenshot_as_png()
print("Binary image data: ", image_bytes)

# Saves a screenshot of the current window to a PNG image file.
# Returns False if there is any IOError, else returns True.
# Use full paths in your filename.
driver.get_screenshot_as_file('screenshot_file.png')

# Gets the screenshot of the current window as a base64 encoded string which is useful in embedded images in HTML
image_base64_str = driver.get_screenshot_as_base64()
print("Base64 encoded string: ", image_base64_str)

driver.close()


driver.quit()