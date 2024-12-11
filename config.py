from selenium import webdriver
from selenium.webdriver.chrome.options import Options
BaseUrl="http://siebelprd.vtr.cl:2080/ecommunications_ldap_esn/start.swe?SWECmd=Login&SWEBHWND=&SRN=&SWEHo=siebelprd.vtr.cl&SWETS=1728285611"
UserName="jresplandor"
Password="CLARO12#"
RUT1 = "15451737-5" #tiene ordenes de servicio
RUT2 = "8912574-k" #sin ordenes
RUT_ORDER = "13942046-2" #tiene ordenes
ORDER = "1-247248431307"

class BrowserSetup:
    def __init__(self):
        self.driver = None

    def initialize_browser(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--disable-web-security')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument('--allow-running-insecure-content')
        chrome_options.add_argument('--no-default-browser-check')
        chrome_options.add_argument('--no-first-run')
        chrome_options.add_argument('--no-proxy-server')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        #self.driver.set_window_size(1280,720) #tamaño ventana
       
        # Modificando agent
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        chrome_options.add_argument(f"user-agent={user_agent}")
        self.driver = webdriver.Chrome(options=chrome_options)
        
        #self.driver = webdriver.Edge()
        return self.driver
    