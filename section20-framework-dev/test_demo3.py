import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass
from pages.home import Home
from pages.checkout import Checkout


class TestTwo(BaseClass):

    def test_form(self,getData):
        driver = TestTwo.driver
        home = Home(driver)
        driver.refresh()
        driver.find_element(By.NAME, "email").send_keys(getData[2])
        driver.find_element(By.ID, "exampleInputPassword1").send_keys(getData[1])
        driver.find_element(By.ID, "exampleCheck1").click()

        # CSS SELECTOR SYNTAX: tagName[attribute='value'] -> input[type='submit']
        driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys(getData[0])

        # XPATH SYNTAX: //tagName[@attribute='value'] -> //input[@type='submit']
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        message = driver.find_element(By.CLASS_NAME, "alert-success").text
        print(message)

        assert "Success" in message

    @pytest.fixture(params=[("Kiranmoy","13579", "kiran@gmail.com"),("Paul","24680", "paul@gmail.com")])
    def getData(self, request):
        return request.param

