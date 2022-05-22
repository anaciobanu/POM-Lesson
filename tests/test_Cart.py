from pages.LoginPage import LoginPage
from utilities.ReadConfig import ReadConfig
from utilities.Logger import Logger
from pages.ProductListPage import ProductListPage
from pages.CartPage import CartPage

class TestCart:
    valid_username = ReadConfig.get_valid_username()
    valid_password = ReadConfig.get_valid_password()
    logger = Logger.get_logger()

    # def test_click_shopping_cart(self, setup):
    #     self.driver = setup
    #     self.login_page = LoginPage(self.driver)
    #     self.login_page.valid_login()
    #     self.product_list_page = ProductListPage(self.driver)
    #     self.product_list_page.add_to_cart()
    #     self.logger.info('Test Case: Go to Cart')
    #     self.cart_page = CartPage(self.driver)
    #     self.cart_page.click_shopping_cart()
    #     if 'your cart' in self.driver.page_source.lower():
    #         assert True
    #     else:
    #         assert False

    def test_remove_item_during_checkout(self, setup):
        self.logger.info('Test Case: Remove item during checkout')  
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.add_to_cart()
        self.cart_page = CartPage(self.driver)
        self.cart_page.click_shopping_cart()
        self.cart_page.click_remove()
        if 'continue-shopping'.lower() in self.driver.page_source.lower():
            assert True
        else:
            assert False
    
    def test_checkout(self, setup):
        self.logger.info('Test Case: Checkout')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.product_list_page = ProductListPage(self.driver)
        self.product_list_page.add_to_cart()
        self.product_list_page.click_shopping_cart()
        self.cart_page = CartPage(self.driver)
        self.cart_page.click_checkout_button()
        if 'Checkout: Your Information'.lower() in self.driver.page_source.lower():
            assert True
        else:
            assert False
