import unittest
from selenium import webdriver
from configparser import ConfigParser
from webdriver_manager.chrome import ChromeDriverManager
from pomLocatorActionInSepratePage.pages.loginPage import LoginPage

class MainTestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.parser = ConfigParser()
        cls.parser.read('../../config/configuration_file.ini')  # Reading data from test.ini file from Utility directory
        print(cls.parser.get('files', 'url_path'))
        cls.driver.get(cls.parser.get('files', 'url_path'))

    def test_01login123(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username("kamal@qafrevvo")
        login.enter_password("qafrevvo")
        login.login_button()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()