from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_bar = (By.ID, "searchBar")
        self.chechkout_button = (By.XPATH,'//*[@id="navbarResponsive"]//a')
        self.carousel_container = (By.ID,"carouselExampleIndicators")
        self.carousel_element= (By.XPATH,'//*[@class="carousel-inner"]')
        self.carousel_next_button = (By.XPATH,'//*[@class="carousel-control-next"]')
        self.carousel_prev_button = (By.XPATH,'//*[@class="carousel-control-prev"]') 
        self.number_input_checkout = (By.XPATH,'//*[@id="exampleInputEmail1"]')
        self.checkout_button_confirm = (By.CSS_SELECTOR,'button.btn.btn-success')
    
    def add_product(self,product):
        XPATH_=f'//app-card[.//a[text()="{product}"]]//button[contains(@class, "btn-info")]'
        self.driver.find_element(By.XPATH,XPATH_).click()

    def capture_price(self,product):
        XPATH_=f'//app-card[.//a[text()="{product}"]]//h5'
        price=self.driver.find_element(By.XPATH,XPATH_).text
        return price
    
    def capture_description(self,product):
        XPATH_=f'//app-card[.//a[text()="{product}"]]//p'
        description=self.driver.find_element(By.XPATH,XPATH_).text
        return description
    
    def move_slider_to(self,position):
        carousel = self.driver.find_element(*self.carousel_element)

        # find next button
        next = self.driver.find_element(*self.carousel_next_button)

        # Localizar el carousel
   
        slide_active = carousel.find_element(By.CSS_SELECTOR,"div.carousel-item.active>img")

        # Determinar el número del slide actual
        num_slide_active= slide_active.get_attribute("alt")
        
        for i in range(3):
            #print(num_slide_active)
            if num_slide_active != position:
                next.click()
                time.sleep(1)
            else:
                break
            num_slide_active= carousel.find_element(By.CSS_SELECTOR,"div.carousel-item.active>img").get_attribute("alt")

        
    def go_to_checkout(self):
        self.driver.find_element(*self.chechkout_button).click()
    
    def confirm_checkout(self):
        self.driver.find_element(*self.checkout_button_confirm).click()
        
    def increase_items(self,items):
        for i in range(items):
            self.driver.find_element(*self.number_input_checkout).send_keys(Keys.ARROW_UP)