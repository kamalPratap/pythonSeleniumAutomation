from time import sleep
from temp2TestScenarios.testBase.multipleBrowser import Browser
from temp2TestScenarios.locators.locatorLoginPage import *


class LoginPage123(Browser):
    def testLoginFrevvo(self):
        driver = self.driver
        login = LoginPageLocators(driver)
        login.enter_username("admin@d")
        login.enter_password("admin")
        login.login_button()
        print("1st Test Case")
        uploadfile1 = UploadFile(driver)
        uploadfile1.manage_default_data()
        sleep(2)
        uploadfile1.choose_file("C:\desktop file\_data.properties")
        sleep(5)
        uploadfile1.upload_button()
        sleep(10)

    def test01LoginFrevvo(self):
        driver = self.driver
        login = LoginPageLocators(driver)
        login.enter_username("kamal@qafrevvo")
        login.enter_password("qafrevvo")
        login.login_button()
        print("1st Test Case")
        sleep(1)

    def test02LoginFrevvo1(self):
        driver = self.driver
        login = LoginPageLocators(driver)
        login.enter_username("kamal@qafrevvo")
        login.enter_password("qafrevvo")
        login.login_button()
        print("2nd Test Case")
        sleep(1)