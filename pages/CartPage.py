from selenium.webdriver.common.by import By

class CartPage:
    text_cart_counter_css = '.shopping_cart_badge'

def __init__(self, driver):
        self.driver = driver

def CartPage(self):
    self.driver.find_element(By. Class, '.shopping_cart_link"'). click()
    
    


