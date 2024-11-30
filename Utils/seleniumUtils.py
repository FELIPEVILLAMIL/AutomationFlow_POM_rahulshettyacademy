from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def wait_element(driver,element):
    WebDriverWait(driver,60).until(EC.visibility_of_element_located(element))
def wait_element_login(driver,element):
    WebDriverWait(driver,120).until(EC.visibility_of_element_located(element))
def wait_element_2_elemts(driver,element1,element2):
    try:
        elementR=WebDriverWait(driver,20).until(EC.any_of(EC.visibility_of_element_located(element1),EC.visibility_of_element_located(element2)))
        print(elementR)
        return elementR
    except Exception as e:
        print(e)
        
def wait_clickable(driver,element):
    for attempts in range(10):
        try:
            time.sleep(1)
            button=WebDriverWait(driver,30).until(EC.element_to_be_clickable(element))
            button.click()
            break
        except Exception as e:
            print(f'{element} was not clickable')
    
            
        