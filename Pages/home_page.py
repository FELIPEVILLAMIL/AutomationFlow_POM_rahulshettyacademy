from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_bar = (By.ID, "searchBar")
        self.search_button = (By.ID, "searchBtn")

    def search_product(self, product_name):
        self.driver.find_element(*self.search_bar).send_keys(product_name)
        self.driver.find_element(*self.search_button).click()
    