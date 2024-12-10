from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Utils.seleniumUtils import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

class OrdersPage:
    def __init__(self, driver):
        self.driver = driver
        self.orders_option = (By.ID,'s_3_1_11_0_mb')
        self.change_rol_button = (By.ID,'s_1_1_1_0_Ctrl')
        self.parameter_dropdown = (By.XPATH,'//*[@id="s_vis_div"]/select')
        self.table_first_element = (By.ID,"1")
        self.search_open_button = (By.ID,'s_2_1_25_0_Ctrl')
        self.specify_query = (By.ID,'2_msg')
        self.click_search_order_type = (By.XPATH,'//*[@id="1_s_2_l_Order_Type"]')
        self.click_search_account = (By.XPATH,'//*[@id="1_s_2_l_Account"]')
        self.search_input_order_type = (By.XPATH, "//input[@name='Order_Type' and @role='input']")
        self.search_input_account = (By.XPATH,'//*[@id="1_Account"]')
        self.table_second_element = (By.ID, "2")
        self.sort_table = (By.XPATH,'//*[@id="jqgh_s_2_l_Created"]')
        self.sort_table_desc = (By.XPATH,'//ul[@id="s_S_A2_headerMenu"]//*[@id="SortDesc"]')
        self.orders_column = (By.XPATH, "//td[contains(@id, '_l_Order_Number')]")
        self.cancel_order =(By.ID,"s_2_1_10_0_Ctrl")
        
        #self.home_button = (By.XPATH,'//a[contains(text(),"Página inicial")]')
        #self.table_rows=(By.XPATH,'//table[@id="s_2_l"]/tbody/tr')
        #self.order_id_field= (By.XPATH,'//*[@id="a_1"]/div/table/tbody/tr[3]/td[3]/div/input')
       

    def change_rol(self):
        self.driver.find_element(*self.change_rol_button).click()

    def open_orders(self):
        self.driver.find_element(*self.orders_option).click()
    
    def select_parameter(self,parameter):
        select = Select(self.driver.find_element(*self.parameter_dropdown))
        select.select_by_visible_text(parameter)
    
    def open_search_option(self):
        self.driver.find_element(*self.search_open_button).click()

    def select_element_to_click(self, element):
        self.driver.find_element(*element).click()
    
    def fill_search_field(self,element,text):
        self.driver.find_element(*element).send_keys(text)

    def click_sort_column(self):
        wait_clickable(self.driver,self.sort_table)
    
    def click_element_desc(self):
        self.driver.find_element(*self.sort_table_desc).click()
        
    def sort_elemets_asc(self):
        wait_clickable(self.driver,self.sort_table_desc)

    def get_order_list(self):
        order_number_cells = self.driver.find_elements(*self.orders_column)
        self.order_numbers = []
        for cell in order_number_cells:
            order_number = cell.text
            self.order_numbers.append(order_number)
            
        print("Números de pedido encontrados:", self.order_numbers)
    
    # Función para verificar la cantidad de elementos en una columna 
    def check_if_orders_in_column(self, column):
        elements = self.driver.find_elements(*column)
        number_of_elements = len(elements)
        return number_of_elements
    
    def search_order(self, OrderNumber):
        try:
            indexN = self.order_numbers.index(OrderNumber)
            print(indexN)
            return indexN
        except ValueError:
            return "Elemento no encontrado"
        
    def get_data(self):
        info = ""
        for attempts in range(5):
            try:
                info = self.driver.find_element(*self.date_first_option).text
                break  
            except Exception as e:
                time.sleep(1)
                print(f' was not reachable on attempt {attempts + 1}')
        return info

    """def change_date_format(self, date_column, date_format = "%Y-%m-%d"):
       date_cells = self.driver.find_elements(date_column)
       timestamps = []
       for cell in date_cells:
            date_text = cell.text.strip()
            try:
                
                date_object = datetime.strptime(date_text, date_format)
                timestamp = int(date_object.timestamp())
                timestamps.append(timestamp)

            except ValueError as e:
                print(f"Error procesando la fecha '{date_text}': {e}")
                timestamps.append(None)  # Manejar celdas con datos no válidos

        return timestamps
    
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
        return messagew.text"""