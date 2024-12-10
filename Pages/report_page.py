from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from Utils.seleniumUtils import *
from selenium.webdriver.support import expected_conditions as EC

class ReportPage():
    def __init__(self, driver):
        self.driver = driver
        #selector pestana agendamiento
        self.booking_information_button = (By.XPATH,'//li//a[contains(text(),"Agendamiento")]') #cual es
        #selectores para recolectar los datos después de realizar la consulta
        self.order_number=(By.XPATH,'//input[@aria-label="Nº de Pedido"]')
        self.order_modality=(By.XPATH,'//input[@aria-label="Modalidad de Venta"]')
        self.order_method=(By.XPATH,'//input[@aria-label="Método de Envío"]')
        self.order_type=(By.XPATH,'//input[@aria-label="Tipo Portado"]')
        self.order_customer_name=(By.XPATH,'//input[@aria-label="Nombre del Cliente"]')
        self.order_account_number=(By.XPATH,'//input[@aria-label="Cuenta del Cliente"]')
        self.order_Status=(By.XPATH,'//input[@aria-label="Estado"]')
        self.order_creation_date=(By.XPATH,'//input[@aria-label="Fecha de creación"]')
        self.order_process_status = (By.XPATH,'//input[@aria-label="Estado del Trámite"]')
        
        #no veo esto donde esta pero hasta aca está bien
        #selectores seccion de agendamiento
        self.booking_WorkTime = (By.XPATH,'//input[@aria-label="Tiempo de trabajo"]')
        self.booking_NoSoonerThan = (By.XPATH,'//input[@aria-label="Inicio más temprano"]')
        self.booking_NoLaterThan = (By.XPATH,'//input[@aria-label="Inicio más tardío"]')
        self.booking_ServiceStreetAddress = (By.XPATH,'//input[@aria-label="Dirección de la cuenta"]')
        self.booking_region = (By.XPATH,'//input[@aria-label="Región"]')
        self.booking_city = (By.XPATH,'//input[@aria-label="Ciudad"]')
        #
        self.booking_OCSDueDate = (By.XPATH,'//input[@aria-label="Fecha Agendamiento"]')
        self.booking_OCSTimeFrom = (By.XPATH,'//input[@aria-label="Hora Desde"]')
        self.booking_OCSTimeTo = (By.XPATH,'//input[@aria-label="Hora Hasta"]')
        self.booking_PostalCode = (By.XPATH,'//input[@aria-label="Código postal"]')
        self.booking_OCSCertfDate = (By.XPATH,'//input[@aria-label="Fecha certificada"]')
        #
        self.booking_RUTTecnico = (By.XPATH,'//input[@aria-label="RUT Técnico"]')
        self.booking_IDTecnico= (By.XPATH,'//input[@aria-label="Id Técnico"]')
        self.booking_TecName= (By.XPATH,'//input[@aria-label="Nombre Técnico"]')
        self.booking_Bucket= (By.XPATH,'//input[@aria-label="Bucket"]')
        self.booking_Territorio= (By.XPATH,'//input[@aria-label="Territorio"]')
        self.booking_Zone= (By.XPATH,'//input[@aria-label="Zona"]')
        self.booking_RedZone= (By.XPATH,'//input[@aria-label="Zona Roja"]')
        #
        self.booking_Notes= (By.XPATH,'//input[@aria-label="Notas"]')
        self.booking_Brand= (By.XPATH,'//input[@aria-label="Marca Técnico"]')
        self.booking_HousingType= (By.XPATH,'//input[@aria-label="Tipo vivienda"]')
        self.booking_HousingClass= (By.XPATH,'//input[@aria-label="Clase vivienda"]')
        
    def open_booking_info(self): #abrir informacion del agendamiento
        wait_clickable(self.driver,self.booking_information_button)
    def get_info(self,element):
        info=""
        for attempts in range(5):
            try:
                info=self.driver.find_element(*element).get_attribute('value')
            except Exception as e:
                time.sleep(1)
                print(f'{element} was not reachable')
        return info
    def copy_booking_info(self):
        user_data = {
            'client':{
                'ActivityId': self.get_info(self.order_ActivityId),
                'Type':self.get_info(self.order_Type),
                'ClientName':self.get_info(self.order_ClientName),
                'ClientRUT':self.get_info(self.order_ClientRUT),
                'Status':self.get_info(self.order_Status),
                'PrimaryOwned':self.get_info(self.order_PrimaryOwned),
                'CreatedBy':self.get_info(self.order_CreatedBy),
                'Reason':self.get_info(self.order_Reason),
                'Planned':self.get_info(self.order_Planned),
                'PlannedEnd':self.get_info(self.order_PlannedEnd),
                'Channel':self.get_info(self.order_Channel),
                'CloseCode':self.get_info(self.order_CloseCode),
                'Motive':self.get_info(self.order_Motive),
                'order_Description':self.get_info(self.order_Description),
                'Comment':self.get_info(self.order_Comment)
                },
            'booking':{
                'WorkTime': self.get_info(self.booking_WorkTime) ,
                'NoSoonerThan': self.get_info(self.booking_NoSoonerThan),
                'NoLaterThan': self.get_info(self.booking_NoLaterThan),
                'ServiceStreetAddress': self.get_info(self.booking_ServiceStreetAddress),
                'region': self.get_info(self.booking_region),
                'city': self.get_info(self.booking_city),
                'DueDate': self.get_info(self.booking_OCSDueDate),
                'TimeFrom': self.get_info(self.booking_OCSTimeFrom),
                'TimeTo': self.get_info(self.booking_OCSTimeTo),
                'PostalCode': self.get_info(self.booking_PostalCode),
                'CertfDate': self.get_info(self.booking_OCSCertfDate),
                'RUTTecnico': self.get_info(self.booking_RUTTecnico),
                'TecName': self.get_info(self.booking_TecName),
                'Bucket': self.get_info(self.booking_Bucket),
                'Territorio': self.get_info(self.booking_Territorio),
                'Zone': self.get_info(self.booking_Zone),
                'RedZone': self.get_info(self.booking_RedZone),
                'Brand': self.get_info(self.booking_Brand),
                'HousingType': self.get_info(self.booking_HousingType),
                'HousingClass': self.get_info(self.booking_HousingClass)
            }
        }
        return user_data

        
        