from selenium.webdriver.common.by import By


class Checkout:

    def __init__(self, webdriver):
        self.driver = webdriver

    products = (By.CSS_SELECTOR, ".card-title a")
    add_product_button = (By.CSS_SELECTOR, ".card-footer button")

    def getAllProducts(self):
        return self.driver.find_elements(*Checkout.products)

    def getAllProductsButton(self):
        return self.driver.find_elements(*Checkout.add_product_button)
