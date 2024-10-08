from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, "#")            # Change username tag if needed
        self.password_textbox = (By.ID, "#")            # Change password tag if needed
        self.login_button = (By.XPATH, "#")             # Change login_button tag if needed
