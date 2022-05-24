import pytest
from selenium import webdriver
from datetime import datetime
from utilities.ReadConfig import ReadConfig
from utilities.logger import Logger
import os 

logger = Logger.get_logger()

@pytest.fixture()
def setup(request, add_pipelines_attachment):
    # the following code runs before each test
    url = ReadConfig.get_app_url()
    driver = webdriver.Firefox()
    logger.info(f'Opening {driver.name} browser')
    driver.maximize_window()
    driver.get(url)
    logger.info(f'Navigating to {url}')
    
    # the following code runs after each test
    def teardown():
        image_name = os.path.join(os.path.abspath(os.path.dirname(__file__)),
        fr".\screenshots\image-{datetime.today().strftime('%m%d%y-%H%M%S')}.png")
        driver.save_screenshot(image_name)
        add_pipelines_attachment(image_name, "testing SwagLabs webpage")
        logger.info(f'Taking a screenshot {image_name}')
        logger.info(f'Closing the browser')
        driver.quit()
    request.addfinalizer(teardown)
    return driver


# it is a hook to add env info
def pytest_configure(config):
    config._metadata['Project Name'] = 'Swag Labs'
    config._metadata['Tester'] = 'Ana'