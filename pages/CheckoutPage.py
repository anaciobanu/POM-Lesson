from typing_extensions import self
from selenium.webdriver.common.by import By

class CheckoutPage:

    # class attributes
    button_checkout_css = '#checkout'
    textbox_first_name_id = '#first-name'
    textbox_last_name_id = 'last-name'
    textbox_postal_code_id= '#postal-code'
    button_continue_id = 'continue'
    button_finish_id = 'finish'

    
    def __init__(self, driver):
        self.driver = driver

    def CheckoutPage_type(self, setup, input_text):
        self.driver.find_element(By.ID, '#checkout').click()
        self.driver.find_element(By.ID,'#first-name').send_keys('Ana')
        self.driver.find_element(By.ID,'#last-name').send_keys('Ciobanu')
        self.driver.find_element(By.ID,'#postal-code').send_keys('45039')
        self.driver.find_element(By.ID,'#continue').click()
        self.driver.find_element(By.ID,'#finish').click()
        self.driver.find_element(By.ID,'.complete-header')
    
    if 'Thank you for your order' in self.driver.page_source.lower():
            assert True
    else:
            assert False


 