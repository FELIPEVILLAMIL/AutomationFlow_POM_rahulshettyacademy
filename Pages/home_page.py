from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Utils.seleniumUtils import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.activities_option = (By.ID,'s_4_1_11_0_mb')
        self.change_rol_button = (By.ID,'s_1_1_1_0_Ctrl')
        self.parameter_dropdown = (By.XPATH,'//*[@id="s_vis_div"]/select')
        self.table_first_element = (By.ID,"1")
        self.search_open_button = (By.ID,'s_2_1_15_0_Ctrl')
        self.search_input_field = (By.XPATH,'//input[@aria-label="RUT Cliente"]')
        self.sort_table = (By.XPATH,'//*[@id="s_2_l_Planned"]')
        self.sort_table_asc = (By.XPATH,'//ul[@id="s_S_A2_headerMenu"]//*[@id="SortAsc"]')
        self.first_element_terreno = (By.XPATH,'//*[@id="1"]//a[contains(text(),"Terreno")]')
        self.home_button = (By.XPATH,'//a[contains(text(),"Página inicial")]')
        self.table_rows=(By.XPATH,'//table[@id="s_2_l"]/tbody/tr')
        self.order_id_field= (By.XPATH,'//input[@aria-label="Id Actividad"]')

    def chage_rol(self):
        self.driver.find_element(*self.change_rol_button).click()
    def open_activities(self):
        self.driver.find_element(*self.activities_option).click()
    
    def select_parameter(self,parameter):
        select = Select(self.driver.find_element(*self.parameter_dropdown))
        select.select_by_visible_text(parameter)
    
    def fill_search_field(self,parameter):
        self.driver.find_element(*self.search_input_field).send_keys(parameter)
    
    def open_search_option(self):
        self.driver.find_element(*self.search_open_button).click()
        
    def click_sort_column(self):
        wait_clickable(self.driver,self.sort_table)
        
    def sort_elemets_asc(self):
        wait_clickable(self.driver,self.sort_table_asc)

    def open_terreno_info(self):
        wait_clickable(self.driver,self.first_element_terreno)
    
    def return_home(self):
        wait_clickable(self.driver,self.home_button)
    
    def get_info(self,element):
        info=""
        for attempts in range(5):
            try:
                time.sleep(1)
                info=self.driver.find_element(*element).get_attribute('value')
                for atts in range(5):
                    if info=="":
                        time.sleep(1)
                        info=self.driver.find_element(*element).get_attribute('value')   
                break
            except Exception as e:
                print(f'{element} was not reachable')
        return info
    
    def check_if_there_are_not_orders(self):
        if self.get_info(self.order_id_field)=="":
            print("No orders")
            return True
        else:
            return False
     
    def check_alert_message(self):
        messagew = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.order_id_field))
        return messagew.text
    
