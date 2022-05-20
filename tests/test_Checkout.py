from os import name
from py import code
from pages.CartPage import CartPage
from pages.LoginPage import LoginPage
from pages.ProductListPage import ProductListPage
from pages.ProductDetailsPage import ProductDetailsPage
from utilities.Logger import Logger
from utilities.ReadConfig import ReadConfig

class Test_Checkout:

    # class attributes
    #textbox_first_name_id = ReadConfig.get_valid.first_name()
    #textbox_last_name_id = ReadConfig.get_valid.last_name()
    #textbox_postal_code_id= ReadConfig.get_valid.postal_code()

    logger = Logger.get_logger()

#class methods = test cases
    def Test_Checkout(self, setup):
        self.logger.info('*** Test Case: Checking out ')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.view_product_details()
        self.product_details_page = ProductDetailsPage(self.driver)
        self.product_details_page.back_to_products()
        self.cart_page = CartPage(self.driver)
        self.cart_page.continue_shopping()

