import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# pytest hook: to handle command-line option
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )

# fixture passing driver object to the test class

@pytest.fixture(scope="class")
def setup(request):                     # pytest provides request parameter for handling runtime properties
    browser = request.config.getoption("browser")
    if browser == 'firefox':
        service_obj = Service("../resources/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    else:
        service_obj = Service("../resources/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    # setting driver variable/property in request parameter
    # now the test method/class will have access to this driver object
    request.cls.driver = driver

    yield
    time.sleep(2)
    driver.close()
