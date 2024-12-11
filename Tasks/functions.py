from config import *
from Utils.seleniumUtils import *
from Pages.LoginPage import LoginPage
from Pages.home_page import HomePage
from Pages.query_page import QueryPage
from Pages.orders_page import OrdersPage
from Pages.report_page import ReportPage
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#from datatime import datatime


def login(driver):
    """Esta funcion sirve para realizar el login y realizar el cambio de rol de forma que el programa quede logueado y en la pagina principal

    Args:
        Driver
    """
    for attempts in range(3):
        try:
            driver.get(BaseUrl)
            driver.execute_script("document.body.style.zoom='67%'") #zoom del 67%
            login_page = LoginPage(driver)
            home_page = HomePage(driver)
            login_page.enter_username(UserName)
            login_page.enter_password(Password)
            login_page.click_login()
            wait_element_login(driver,home_page.change_rol_button)
            home_page.chage_rol()
            wait_element_login(driver,home_page.activities_option)
            print("login exitoso")
            break
            
        except Exception as e:
            driver.save_screenshot("images/test_bad_login.png")
            print("no se pudo iniciar sesion")
            driver.delete_all_cookies()
            print(e)
    return "login failed"
    

def search_info_user(driver,Rut):
    """Esta funcion es usada para realizar la busqueda y recoleccion de los datos de un usuario identificado por un RUT unico

    Args:
        driver (driver): _description_
        Rut : es una cadena de texto con el RUT a consultar
    """
    try:
        home_page = HomePage(driver)
        query_page = QueryPage(driver)
        wait_element(driver,home_page.activities_option)
        home_page.open_activities()
        wait_element(driver,home_page.parameter_dropdown)
        home_page.select_parameter("Todas las actividades")
        wait_element(driver,home_page.table_first_element)
        home_page.open_search_option()
        wait_element(driver,home_page.table_first_element)
        home_page.fill_search_field(Rut)
        #enter manual
        ActionChains(driver).key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
        wait_element(driver,home_page.table_first_element)
        wait_element(driver,home_page.sort_table)
        if home_page.check_if_there_are_not_orders() :
            datos_usuario = {}
            home_page.return_home()
            wait_element(driver,home_page.activities_option)
            return datos_usuario #then return empty dictionary
        # click in sort column
        home_page.click_sort_column()
        wait_element(driver,home_page.sort_table_asc)
        #sort elements
        home_page.sort_elemets_asc()
        wait_element(driver,home_page.first_element_terreno)
        #click terreno
        home_page.open_terreno_info()
        wait_element(driver,query_page.booking_information_button)
        query_page.open_booking_info()
        wait_element(driver,query_page.booking_WorkTime)
        datos_usuario=query_page.copy_booking_info()
        home_page.return_home()
        wait_element(driver,home_page.activities_option)
        return datos_usuario
    except Exception as e:
        print("failed consultation")
        datos_usuario={}
        return datos_usuario
    

def orders_info_user(driver,Rut):
    """Esta funcion es usada para realizar la busqueda y recoleccion de los datos de un usuario identificado por un RUT unico

    Args:
        driver (driver): _description_
    """
    try:
        orders_page = OrdersPage(driver)
        report_page = ReportPage(driver)
        wait_element(driver,orders_page.orders_option)
        orders_page.open_orders() 
        wait_element(driver,orders_page.parameter_dropdown)
        orders_page.select_parameter("Todos los pedidos de ventas") 
        wait_element(driver,orders_page.table_first_element)
        orders_page.open_search_option()
        wait_element(driver,orders_page.specify_query)
        orders_page.select_element_to_click(orders_page.click_search_order_type)
        time.sleep(2)
        orders_page.fill_search_field(orders_page.search_input_order_type,"Pedido de ventas")
        orders_page.select_element_to_click(orders_page.click_search_account)
        orders_page.fill_search_field(orders_page.search_input_account,Rut)
        #enter
        ActionChains(driver).key_down(Keys.RETURN).key_up(Keys.RETURN).perform() 
        
        wait_button_is_disabled(driver,orders_page.cancel_order)
        print("paso el wait")
        if (orders_page.check_if_orders_in_column(orders_page.orders_column)==0):
            print("no hay elementos")
            return "No hay ordenes con ese numero de RUT"
        wait_element(driver,orders_page.sort_table)
        orders_page.click_sort_column()
        wait_element(driver,orders_page.sort_table_desc)
        orders_page.click_element_desc()
        print("Llego aquí")
        time.sleep(10)
        orders_page.get_order_list()
        time.sleep(10)
        orders_page.search_order("1-247248431307")
        orders_page.get_order_data("1-247248431307")
        time.sleep(1000)

        #wait_element(driver,orders_page.) #no se como darle la espera para que organice la tabla
        #orders_page.change_date_format()
        
        
    except Exception as e:
        print("failed orders")
        print(e)
        

def logout(driver):
    time.sleep(1)
    # Ejecutar el shortcut CTRL + SHIFT + X
    ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('x').key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()
    print("FIN")

    
