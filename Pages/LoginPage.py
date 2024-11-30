from selenium.webdriver.common.by import By
import time
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, '//input[@name="SWEUserName"]')
        self.password_input = (By.XPATH, '//input[@name="SWEPassword"]')
        self.login_button = (By.ID,"s_swepi_22")
        self.wrong_password_message = (By.XPATH,'//*[@id="statusBar"]')#/br[1]')

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)
    
    def clear_username(self):
        self.driver.find_element(*self.username_input).clear()
    
    def clear_password(self):
        self.driver.find_element(*self.password_input).clear()

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        

            