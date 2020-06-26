import unittest
import datetime
from selenium import webdriver
from configparser import ConfigParser
from webdriver_manager.chrome import ChromeDriverManager


class Browser(unittest.TestCase):
    def setUp(self):
        print("Run Start at:- "+str(datetime.datetime.now()))
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        parser = ConfigParser()
        parser.read('../../config/configuration_file.ini')  # Reading data from test.ini file from Utility directory
        print(parser.get('files', 'url_path'))
        self.driver.get(parser.get('files', 'url_path'))

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Run Completed at:- " + str(datetime.datetime.now()))
