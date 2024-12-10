from config import *
from Tasks.functions import *
#import logging

    
def main():
    # Config
    browser_setup=BrowserSetup()
    driver = browser_setup.initialize_browser()
    # Login functionality
    login(driver)
    # findind the INFORMATION USING THE RUT
    #print(search_info_user(driver,RUT1))
    orders_info_user(driver,RUT_ORDER)
    print("Logramos las ordenes")
    #consulta RUT sin ordenes
    #print(search_info_user(driver,RUT2))
    #funcion opcional si se requiere hacer logout
    #logout(driver)
    driver.quit()

if __name__ == "__main__":
    main()