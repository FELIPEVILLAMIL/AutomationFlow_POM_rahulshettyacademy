import pytest
from configtest import *
from Utils.seleniumUtils import *
from Pages.LoginPage import LoginPage


@pytest.mark.usefixtures("browser_setup")
class Test_Login:
    def setup_class(self):
        self.driver.get(BaseUrl+"loginpagePractise/")
        self.login_page = LoginPage(self.driver)
        
    def test_invalid_login(self):
        self.login_page.enter_username(UserName)
        self.login_page.enter_password(WrongPassword)
        self.login_page.click_profile_user()
        prompt_message=self.login_page.accept_prompt_message()
        assert prompt_message == 'You will be limited to only fewer functionalities of the app. Proceed?', "Different message"
        print(prompt_message)
        self.login_page.select_role("teach")
        self.login_page.mark_checkbox()
        self.login_page.click_login()
        alert = self.login_page.check_alert_message()
        self.driver.save_screenshot("images/test_invalid_login.png")
        assert alert == "Incorrect username/password.","Different message"
        print('The invalid message is equal to the information shown.')
        
        
        
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

    def teardown_class(self):
        self.driver.quit()