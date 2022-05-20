from selenium.webdriver.common.by import By
from pages.CartPage import CartPage

class ProductListPage:

    # class attributes
    button_inventory_css = '.btn_inventory'
    text_cart_counter_css = '.shopping_cart_badge'
    text_inventory_item_name_css = '.inventory_item_name'

    # class constructor, initializer
    def __init__(self, driver):
        self.driver = driver
    
    # class method, actions, behavior
    def choose_item_name(self,driver):
        product_names = self.driver.find_elements(By.CSS_SELECTOR, self.text.inventory_item_name_css)
        product_names[0].self.driver.click()
        self.driver.find_element(By. ID, '#add-to-CartPage-sauce-labs-backpack').click()


   
 
    