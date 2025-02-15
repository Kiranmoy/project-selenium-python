import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        driver = self.driver
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
        driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        driver.find_element(By.LINK_TEXT, "India").click()
        driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        success_msg = driver.find_element(By.CSS_SELECTOR, ".alert-success").text

        print(success_msg)
        assert "Success" in success_msg
