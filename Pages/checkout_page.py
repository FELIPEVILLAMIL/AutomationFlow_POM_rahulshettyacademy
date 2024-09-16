from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.XPATH,'//*[@id="navbarResponsive"]//a')
        self.delivery_location_field=(By.ID,'country')
        self.purchase_button = (By.CSS_SELECTOR,"input[type='submit'][value='Purchase']")
        self.purchase_alert = (By.CSS_SELECTOR,"div.alert.alert-success")

    
    def fill_delivery_location(self,country):
        self.driver.find_element(*self.delivery_location_field).send_keys(country)
    
    def confirm_purchase(self):
        self.driver.find_element(*self.purchase_button).click()
    
    def check_alert_message(self):
        message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.purchase_alert))
        return message.text
    
    def get_checkout_amount(self):
        amount = self.driver.find_element(*self.checkout_button)
        number = re.findall(r'\d+', amount.text)
        print(number[0])
        return number[0]