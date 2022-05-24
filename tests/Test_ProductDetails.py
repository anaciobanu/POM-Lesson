from pages.LoginPage import LoginPage
from utilities.ReadConfig import ReadConfig
from utilities.logger import Logger
from pages.ProductDetailsPage import ProductDetailsPage


class TestProductDetails:
    # valid_username = ReadConfig.get_valid_username()
    # valid_password = ReadConfig.get_valid_password()
    logger = Logger.get_logger()

    def test_product_details(self, setup):
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.logger.info('Test Case: Check product details')
        self.product_details_page = ProductDetailsPage(self.driver)
        self.product_details_page.view_product_details()
        if 'back to products' in self.driver.page_source.lower():
            assert True
        else:
            assert False

    def test_add_to_cart_from_details_page(self, setup):
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.product_details_page = ProductDetailsPage(self.driver)
        self.product_details_page.view_product_details()
        self.logger.info('Test Case: Add to Cart ')
        # self.product_details_page = ProductDetailsPage(self.driver)
        self.product_details_page.add_to_cart()
        if 'remove' in self.driver.page_source.lower():
            assert True
        else:
            assert False

    