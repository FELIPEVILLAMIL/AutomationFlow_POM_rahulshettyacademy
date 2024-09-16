import pytest
from selenium import webdriver
from configtest import *
from Utils.seleniumUtils import *
from Pages.LoginPage import LoginPage
from Pages.product_page import ProductPage
from Pages.checkout_page import CheckoutPage
import pytest_check as check
import time

@pytest.mark.usefixtures("browser_setup")
class Test_Checkout:
    def setup_class(self):
        self.driver.get(BaseUrl+"loginpagePractise/")
        self.login_page = LoginPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
    def test_valid_login(self):
        self.login_page.clear_username()
        self.login_page.clear_password()
        self.driver.save_screenshot("images/test_clean_login.png")
        self.login_page.enter_username(UserName)
        self.login_page.enter_password(Password)
        self.login_page.click_profile_admin()
        self.login_page.select_role("consult")
        self.driver.save_screenshot("images/test_valid_login.png")
        self.login_page.click_login()
        wait_element(self.driver,self.product_page.carousel_container)
        
    def test_add_to_cart(self):
        #add to cart
        self.product_page.add_product("Nokia Edge")
        #get price
        price = self.product_page.capture_price("Nokia Edge")
        print(price)
        #get description
        description = self.product_page.capture_description("Nokia Edge")
        print(description)
        self.product_page.move_slider_to("Second slide")
        self.driver.save_screenshot("images/test_slider.png")
        self.product_page.go_to_checkout()
        wait_element(self.driver,self.product_page.number_input_checkout)
        self.product_page.increase_items(2)
        self.driver.save_screenshot("images/test_checkout.png")
        time.sleep(2)
    
    def test_finish_checkout(self):
        self.product_page.confirm_checkout()
        wait_element(self.driver,self.checkout_page.checkout_button)
        self.checkout_page.fill_delivery_location("Colombia")
        self.checkout_page.confirm_purchase()
        message=self.checkout_page.check_alert_message()
        valid_message="Congratulations! Your order has been placed; it will be delivered between 1-3 business days."
        check.equal( message , valid_message,"The text shown is not what you expected; please review the test case.")
        valid_checkout_info = 0
        checkout_amount = int(self.checkout_page.get_checkout_amount())
        check.equal( checkout_amount , valid_checkout_info, f'Checkout continues at <<{checkout_amount}>>')
        self.driver.save_screenshot("images/test_checkout_amount.png")
        time.sleep(2)
        

    def teardown_class(self):
        self.driver.quit()
