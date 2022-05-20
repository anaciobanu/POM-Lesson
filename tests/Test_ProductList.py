from pages.LoginPage import LoginPage
from pages.ProductListPage import ProductListPage
from utilities.Logger import Logger

class TestProductList:

    # class attributes
    logger = Logger.get_logger()

    # class methods = test cases
    def test_choose_your_product(self, setup):
        self.logger.info('*** Test Case: Choose your product')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.valid_username)
        self.login_page.set_password(self.valid_password)
        self.login_page.click_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.add_to_cart()
        if 'Back to products' in self.driver.page_source.lower():
            assert True
        else:
            assert False
        
  
    
  