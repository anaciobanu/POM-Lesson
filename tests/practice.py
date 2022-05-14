from pages.LoginPage import LoginPage
from utilities.ReadConfig import ReadConfig
from utilities.Logger import Logger
import logging
class TestLogin:

    #class attributes
    valid_username = ReadConfig.get_valid_username()
    valid_password = ReadConfig.get_valid_password()

    logger = Logger.get_logger()
# class methods = test cases
    def test_login_page_title(self, setup):
        self.logger.info('Verifying Home Page Title')
        self.driver = setup
        if page_title == 'Swag Labs':
            self.logger.info('Home Page Title as expected')
            assert True
        else:
            self.logger.info('Home Page Title NOT as expected')
            assert False

    def test_login(self, setup):
        self.logger.info('Verifying Login')
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.valid_username)
        self.lp.set_password(self.valid_password)
        self.lp.click_login()
        page_source = self.driver.page_source
        if 'products' in page_source.lower():
            self.logger.info('Login successfull')
            assert True
        else:
            self.logger.info('Login Failed')
            assert False

