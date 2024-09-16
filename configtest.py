import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
BaseUrl="https://rahulshettyacademy.com/"
UserName="rahulshettyacademy"
Password="learning"
WrongPassword="UniqueTest02}"
@pytest.fixture(scope="class",autouse=True)
def browser_setup(request):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    request.cls.driver=webdriver.Chrome(options=chrome_options)
    