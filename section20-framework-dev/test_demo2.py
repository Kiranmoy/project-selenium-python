import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass
from pages.home import Home
from pages.checkout import Checkout


class TestOne(BaseClass):
    def test_e2e(self):
        driver = TestOne.driver
        home = Home(driver)
        # //a[contains(@href,'shop')]   a[href*='shop']
        home.shopItems().click()

        # Add Blackberry Phone to Cart & Checkout
        checkout = Checkout(driver)
        products = checkout.getAllProducts()
        i = -1
        for product in products:
            i = i + 1
            productName = product.text
            if productName == "Blackberry":
                checkout.getAllProductsButton()[i].click()

        driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        driver.find_element(By.ID, "country").send_keys("ind")
        self.verifyLinkPresence("India")
        driver.find_element(By.LINK_TEXT, "India").click()
        driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        success_msg = driver.find_element(By.CSS_SELECTOR, ".alert-success").text

        print(success_msg)
        assert "Success" in success_msg

    def test_form(self):
        driver = TestOne.driver
        home = Home(driver)
        driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
        driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
        driver.find_element(By.ID, "exampleCheck1").click()

        # CSS SELECTOR SYNTAX: tagName[attribute='value'] -> input[type='submit']
        driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Kiranmoy Paul")

        # XPATH SYNTAX: //tagName[@attribute='value'] -> //input[@type='submit']
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        message = driver.find_element(By.CLASS_NAME, "alert-success").text
        print(message)

        driver.close()

        assert "Successs" in message
