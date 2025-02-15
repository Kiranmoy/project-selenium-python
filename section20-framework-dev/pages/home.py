from selenium.webdriver.common.by import By


class Home:

    def __init__(self, webdriver):
        self.driver = webdriver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
        return self.driver.find_element(*Home.shop) # * - for deserializing them from tuple
