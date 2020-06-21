import time

from pyshadow.main import Shadow
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://localhost:8082/frevvo/web/login")
driver.find_element_by_id("username").send_keys("kamal@qafrevvo")
driver.find_element_by_id("password").send_keys("qafrevvo")
driver.find_element_by_id("login-button").click()
#time.sleep(2)
#driver.find_element_by_xpath("//button[@class='_hj-2qaGY__styles__openStateToggle']").click()

driver.find_element_by_xpath("//a[@title='Add new content']").click()
driver.find_element_by_xpath("//a/paper-icon-item/iron-icon[@icon='frevvo-ui-icons:create-new-folder']").click()

time.sleep(1)
shadow = Shadow(driver)
shadow.find_element("frevvo-ui-wizard-dialog>frevvo-ui-project-wizard>paper-input-container#container>iron-input.input-element>input").send_keys("Prj123")
time.sleep(1)
shadow.find_element("frevvo-ui-wizard-dialog#project-wizard>paper-dialog#wizardDialog>div#wizardButtons>paper-button#finishButton").click()

time.sleep(1)
driver.find_element_by_xpath("//a[@title='Add new content']").click()
driver.find_element_by_xpath("//a/paper-icon-item/iron-icon[@icon='frevvo-ui-icons:workflow-2']").click()

time.sleep(1)
shadow.find_element("frevvo-ui-wizard-dialog#workflow-wizard>frevvo-ui-workflow-wizard>paper-input-container#container>iron-input.input-element>input").send_keys("Workflow123")
time.sleep(1)
shadow.find_element("frevvo-ui-wizard-dialog#workflow-wizard>paper-dialog#wizardDialog>div#wizardButtons>paper-button#nextButton").click()

time.sleep(1)
shadow.find_element("frevvo-ui-wizard-dialog#workflow-wizard>frevvo-ui-workflow-wizard>paper-icon-button#add-steps-icon").click()
time.sleep(1)
shadow.find_element("frevvo-ui-wizard-dialog#workflow-wizard>paper-dialog#wizardDialog>div#wizardButtons>paper-button#finishButton").click()
