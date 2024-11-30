from config import *
from Utils.seleniumUtils import *
from Pages.LoginPage import LoginPage
from Pages.home_page import HomePage
from Pages.query_page import QueryPage
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def login(driver):
    """Esta funcion sirve para realizar el login y realizar el cambio de rol de forma que el programa quede logueado y en la pagina principal

    Args:
        Driver
    """
    for attempts in range(3):
        try:
            driver.get(BaseUrl)
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

def logout(driver):
    time.sleep(1)
    # Ejecutar el shortcut CTRL + SHIFT + X
    ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('x').key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()
    print("FIN")

    
