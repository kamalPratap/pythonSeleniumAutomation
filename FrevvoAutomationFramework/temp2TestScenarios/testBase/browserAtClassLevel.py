import unittest
import datetime
from selenium import webdriver
from configparser import ConfigParser
from webdriver_manager.chrome import ChromeDriverManager


class Browser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Run Start at:- "+str(datetime.datetime.now()))
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        parser = ConfigParser()
        parser.read('../../config/configuration_file.ini')  # Reading data from test.ini file from Utility directory
        print(parser.get('files', 'url_path'))
        cls.driver.get(parser.get('files', 'url_path'))

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Run completed at:- " + str(datetime.datetime.now()))
