class LoginPageLocators():

    # login page
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = "username"
        self.password_textbox_id = "password"
        self.login_button_id = "login-button"

    def enter_username(self,username1):
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username1)

    def enter_password(self,password1):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password1)

    def login_button(self):
        self.driver.find_element_by_id(self.login_button_id).click()


class UploadFile():

    #Upload _data.properties file for manage default data
    def __init__(self,driver):
        self.driver = driver
        self.manage_default_data_button_xpath = "//a[text()='Manage Default _data']"
        self.choose_file_xpath = "//input[@id='props-file' and @name='props-file']"
        self.upload_button_xpath = "//input[@class='input field' and @value='Upload']"

    def manage_default_data(self):
        self.driver.find_element_by_xpath(self.manage_default_data_button_xpath).click()

    def choose_file(self,filename):
        self.driver.find_element_by_xpath(self.choose_file_xpath).send_keys(filename)

    def upload_button(self):
        self.driver.find_element_by_xpath(self.upload_button_xpath).click()