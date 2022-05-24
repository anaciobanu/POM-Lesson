from pages.LoginPage import LoginPage
from utilities.ReadConfig import ReadConfig
from utilities.logger import Logger
from pages.ProductListPage import ProductListPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage

class Test_Checkout:
    valid_username = ReadConfig.get_valid_username()
    valid_password = ReadConfig.get_valid_password()
    firstname = ReadConfig.get_firstname()
    lastname = ReadConfig.get_lastname()
    zipcode = ReadConfig.get_zipcode()

    logger = Logger.get_logger()

    # def test_click_checkout(self, setup):
    #     self.driver = setup
    #     self.login_page = LoginPage(self.driver)
    #     self.login_page.valid_login()
    #     self.product_list_page = ProductListPage(self.driver)
    #     self.product_list_page.add_to_cart()
    #     self.product_list_page.click_shopping_cart()
    #     self.cart_page = CartPage(self.driver)
    #     self.cart_page.click_checkout_button()
    #     self.logger.info('Test Case: Go to Checkout')
    #     self.checkout_page = CheckoutPage(self.driver)
    #     self.checkout_page.click_checkout()
    #     if 'your information' in self.driver.page_source.lower():
    #         assert True
    #     else:
    #         assert False

    def test_complete_checkout_info_and_continue(self, setup):
        self.logger.info('Test Case: Enter Customer information and Continue')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.add_to_cart()
        self.product_list_page.click_shopping_cart()
        self.cart_page = CartPage(self.driver)
        self.cart_page.click_checkout_button()
        self.checkout_page = CheckoutPage(self.driver)
        # self.checkout_page.click_checkout()
        self.checkout_page.set_firstname(self.firstname)
        self.checkout_page.set_lastname(self.lastname)
        self.checkout_page.set_zipcode(self.zipcode)
        # self.logger.info('Test Case: Checking out')
        self.checkout_page.click_continue()
        if 'Checkout: Overview'.lower() in self.driver.page_source.lower():
            assert True
        else:
            assert False

    def test_cancel_checkout(self, setup):
        self.logger.info('Test Case:Cancel checkout')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.add_to_cart()
        self.product_list_page.click_shopping_cart()
        self.cart_page = CartPage(self.driver)
        self.cart_page.click_checkout_button()
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.set_firstname(self.firstname)
        self.checkout_page.set_lastname(self.lastname)
        self.checkout_page.set_zipcode(self.zipcode)
        self.checkout_page.click_cancel()
        if 'Your Cart'.lower() in self.driver.page_source.lower():
            assert True
        else:
            assert False

    def test_finish_checkout(self, setup):
        self.logger.info('Test Case:Finish checkout')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.add_to_cart()
        self.product_list_page.click_shopping_cart()
        self.cart_page = CartPage(self.driver)
        self.cart_page.click_checkout_button()
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.set_firstname(self.firstname)
        self.checkout_page.set_lastname(self.lastname)
        self.checkout_page.set_zipcode(self.zipcode)
        self.checkout_page.click_continue()
        self.checkout_page.click_finish()
        if 'Checkout: Complete!'.lower() in self.driver.page_source.lower():
            assert True
        else:
            assert False

    