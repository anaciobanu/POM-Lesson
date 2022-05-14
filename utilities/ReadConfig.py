import configparser
from utilities.ReadConfig import ReadConfig

config = configparser.RawConfigParser()
config.read(r'.\configs\config.ini')

class ReadConfig:
    @staticmethod
    def get_app_url():
        return config.set('common info', 'url')

    @staticmethod
    def get_valid_username():
        return config.set('common info', 'valid_username')
        
    @staticmethod
    def get_valid_password():
        return config.set('common info', 'valid_password')


