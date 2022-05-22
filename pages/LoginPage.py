from selenium.webdriver.common.by import By
from utilities.ReadConfig import ReadConfig

class LoginPage:

    #class attributes
    textbox_username_id = 'user-name'
    textbox_password_id = 'password'
    button_login_id = 'login-button'
    valid_username = ReadConfig.get_valid_username()
    valid_password = ReadConfig.get_valid_password()

   #class constructor, initializer
    def __init__(self, driver):
        self.driver = driver

#class method,actions, behavior
    def set_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def set_password(self, password):    
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.button_login_id).click()

    def valid_login(self):
        self.set_username(self.valid_username)
        self.set_password(self.valid_password)
        self.click_login()
     


     
