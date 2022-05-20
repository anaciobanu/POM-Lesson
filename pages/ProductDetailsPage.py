from selenium.webdriver.common.by import By

class ProductDetailsPage:

    # class attributes
    button_back_to_products_css = '#back-to-products'
    

    # class constructor, initializer
    def __init__(self, driver):
        self.driver = driver
    
    # class method, actions, behavior
    def back_to_products(self):
        self.driver.find_element(By.CSS_SELECTOR,'#back-to-products').click()
       
