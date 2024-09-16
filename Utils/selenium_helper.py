import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class seleniumHelper:
    def __init__(self,driver):
        self.driver=driver
    def take_screenshot(self,driver):
        if not os.path.exists("Screenshots"):
            os.makedirs("Screenshots")
    def wait_element(self,element):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element))