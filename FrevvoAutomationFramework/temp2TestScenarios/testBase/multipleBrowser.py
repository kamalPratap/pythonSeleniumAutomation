import unittest
from time import sleep
import datetime
from selenium import webdriver
from configparser import ConfigParser
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager


class Browser(unittest.TestCase):
    def setUp(self):
        print("Run Start at:- "+str(datetime.datetime.now()))
        configParser = ConfigParser()
        configParser.read('../../config/configuration_file.ini')
        default_brower = configParser.get('setting', 'default_browser')
        print(type(default_brower))
        print(default_brower.casefold())

        # casefold() string method is used to implement caseless string matching. i.e ignore cases when comparing.
        if default_brower.casefold() == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        elif default_brower.casefold() == "firefox":
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif default_brower.casefold() == "edge":
            self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        elif default_brower.casefold() == "ie":
            self.driver = webdriver.Ie(IEDriverManager().install())
        else:
            print("Browser is not mentioned properly")
        self.driver.maximize_window()
        sleep(5)

        configParser.read('../../config/configuration_file.ini')  # Reading data from test.ini file from Utility directory
        print(configParser.get('files', 'url_path'))
        self.driver.get(configParser.get('files', 'url_path'))

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Run Completed at:- " + str(datetime.datetime.now()))
