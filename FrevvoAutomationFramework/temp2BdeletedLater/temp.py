import time
import unittest
from selenium import webdriver
from pyshadow.main import Shadow
from webdriver_manager.chrome import ChromeDriverManager
from configparser import ConfigParser
import HtmlTestRunner
from pomLocatorActionInSepratePage.pages.loginPage import LoginPage

class MainTestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.parser = ConfigParser()
        cls.parser.read('../config/configuration_file.ini')  # Reading data from test.ini file from Utility directory
        print(cls.parser.get('files', 'url_path'))
        cls.driver.get(cls.parser.get('files', 'url_path'))
        login = LoginPage(cls.driver)
        login.username_textbox_id("kamal@qafrevvo")
        login.password_textbox_id("qafrevvo")
        login.login_button().click()

        # cls.driver.find_element_by_id("username").send_keys("kamal@qafrevvo")
        # cls.driver.find_element_by_id("password").send_keys("qafrevvo")
        # cls.driver.find_element_by_id("login-button").click()

    def test_01CreateProjectWithWF(self):
        time.sleep(2)
        #self.driver.find_element_by_xpath("//button[@class='_hj-2qaGY__styles__openStateToggle']").click()

        self.driver.find_element_by_xpath("//a[@title='Add new content']").click()
        self.driver.find_element_by_xpath("//a/paper-icon-item/iron-icon[@icon='frevvo-ui-icons:create-new-folder']").click()

        time.sleep(1)
        shadow = Shadow(self.driver)
        shadow.find_element("frevvo-ui-wizard-dialog>frevvo-ui-project-wizard>paper-input-container#container>iron-input.input-element>input").send_keys("Prj123")
        time.sleep(2)
        shadow.find_element("frevvo-ui-wizard-dialog#project-wizard>paper-dialog#wizardDialog>div#wizardButtons>paper-button#finishButton").click()

        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@title='Add new content']").click()
        self.driver.find_element_by_xpath("//a/paper-icon-item/iron-icon[@icon='frevvo-ui-icons:workflow-2']").click()

        time.sleep(1)
        shadow.find_element("frevvo-ui-wizard-dialog#workflow-wizard>frevvo-ui-workflow-wizard>paper-input-container#container>iron-input.input-element>input").send_keys("Workflow123")
        time.sleep(1)
        shadow.find_element("frevvo-ui-wizard-dialog#workflow-wizard>paper-dialog#wizardDialog>div#wizardButtons>paper-button#nextButton").click()

        time.sleep(1)
        shadow.find_element("frevvo-ui-wizard-dialog#workflow-wizard>frevvo-ui-workflow-wizard>paper-icon-button#add-steps-icon").click()
        time.sleep(1)
        shadow.find_element("frevvo-ui-wizard-dialog#workflow-wizard>paper-dialog#wizardDialog>div#wizardButtons>paper-button#finishButton").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div/a[@title='Go to home page']").click()  # Click on FREVVO logo

    def test_02CreateWFAddToNewProject(self):
        self.driver.find_element_by_xpath("//a[@title='Add new content']").click()
        self.driver.find_element_by_xpath("//a/paper-icon-item/iron-icon[@icon='frevvo-ui-icons:workflow-2']").click()

        shadow = Shadow(self.driver)
        time.sleep(2)
        shadow.find_element("frevvo-ui-wizard-dialog#workflow-wizard>frevvo-ui-workflow-wizard>frevvo-ui-project-action-screen#project-action-screen>div#projectTypeScreen>paper-button.select-button.button").click()
        time.sleep(2)
        shadow.find_element("frevvo-ui-wizard-dialog#workflow-wizard>frevvo-ui-workflow-wizard>paper-input-container#container>iron-input.input-element>input").send_keys("Prj1234")
        time.sleep(1)
        shadow.find_element("frevvo-ui-wizard-dialog#workflow-wizard>paper-button#nextButton").click()
        time.sleep(1)
        shadow.find_element("frevvo-ui-wizard-dialog#workflow-wizard>frevvo-ui-workflow-wizard>paper-input-container#container>iron-input.input-element>input").send_keys("Workflow123")
        time.sleep(1)
        shadow.find_element("frevvo-ui-wizard-dialog#workflow-wizard>paper-button#nextButton").click()
        time.sleep(1)
        shadow.find_element("frevvo-ui-wizard-dialog#workflow-wizard>frevvo-ui-workflow-wizard>paper-icon-button#add-steps-icon").click()
        time.sleep(1)
        shadow.find_element("frevvo-ui-wizard-dialog#workflow-wizard>paper-button#finishButton").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div/a[@title='Go to home page']").click()       #Click on FREVVO logo

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))
