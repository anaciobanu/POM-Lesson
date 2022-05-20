from pages.LoginPage import LoginPage
from utilities.ReadConfig import ReadConfig
from utilities.Logger import Logger
from pages.CartPage import CartPage
from pages.ProductListPage import ProductListPage
from pages.ProductDetailsPage import ProductDetailsPage

class Test_Cart:

    # class attributes
    logger = Logger.get_logger()

def Test_Cart(self, setup):
        self.logger.info('*** Test Case: Cart page ')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.view_product_details()
        self.product_details_page = ProductDetailsPage(self.driver)
        self.product_details_page.back_to_products()
        self.cart_page = CartPage(self.driver)
    

if 'Continue Shopping' in self.driver.page_source.lower():
    assert True
else:
    assert False