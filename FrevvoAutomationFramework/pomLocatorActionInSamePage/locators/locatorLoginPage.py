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