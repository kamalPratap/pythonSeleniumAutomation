from time import sleep
from pomLocatorActionInSamePage.testBase.browserAtMethodLevel import Browser
#from pomLocatorActionInSamePage.testBase.browserAtClassLevel import Browser
from pomLocatorActionInSepratePage.pages.loginPage import LoginPage


class LoginPage123(Browser):
    def testLoginFrevvo(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username("kamal@qafrevvo")
        login.enter_password("qafrevvo")
        login.login_button()
        sleep(10)


    def testLoginFrevvo1(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username("kamal@qafrevvo")
        login.enter_password("qafrevvo")
        login.login_button()
        sleep(10)