from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, "#")            # Change username tag if needed
        self.password_textbox = (By.ID, "#")            # Change password tag if needed
        self.login_button = (By.XPATH, "#")             # Change login_button tag if needed

    def open_webpage(self, url):
        self.driver.get(url)

    def input_username(self, username):
        self.driver.find_element(self.username_textbox).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(self.login_button).click()