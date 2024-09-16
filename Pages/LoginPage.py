from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "signInBtn")
        self.login_profile_admin = (By.XPATH, '//input[@type="radio" and @value="admin"]')
        self.login_profile_user = (By.XPATH, '//input[@type="radio" and @value="user"]')
        self.ckeckbox_confirmation = (By.ID, "terms")
        self.dropdown_menu = (By.XPATH,'//select[@class="form-control" and @data-style="btn-info"]')
        self.message_window= (By.XPATH,'//div[@class="modal-body"]')
        self.okay_button=(By.ID, "okayBtn")
        self.alert_incorrect_user_pass=(By.CSS_SELECTOR, "div.alert.alert-danger.col-md-12")

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
        
    def click_profile_admin(self):
        self.driver.find_element(*self.login_profile_admin).click()
    
    def click_profile_user(self):
        self.driver.find_element(*self.login_profile_user).click()
    
    def mark_checkbox(self):
        self.driver.find_element(*self.ckeckbox_confirmation).click()
    
    def select_role(self,role):
        select = Select(self.driver.find_element(*self.dropdown_menu))
        select.select_by_value(role)
    
    def check_alert_message(self):
        message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.alert_incorrect_user_pass))
        return message.text
    
    def accept_prompt_message(self):
        try:
            message_window_elem=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.message_window))
            time.sleep(2)
            prompt_message = message_window_elem.text
            self.driver.find_element(*self.okay_button).click()
            return prompt_message
        except Exception as e:
            print(f"An error occurred: {e}")
            