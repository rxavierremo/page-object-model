from selenium.webdriver.common.by import By
<<<<<<< HEAD
from selenium.webdriver.common.keys import Keys
=======
>>>>>>> 23361caa604fdfd423541970d16f9b977085b42f

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
<<<<<<< HEAD
        self.username_textbox = (By.CSS_SELECTOR, "input[placeholder='username']")            # Change username tag if needed
        self.password_textbox = (By.CSS_SELECTOR, "input[placeholder='password']" )            # Change password tag if needed
=======
        self.username_textbox = (By.CSS_SELECTOR, "input[placeholder='Username']")            # Change username tag if needed
        self.password_textbox = (By.CSS_SELECTOR, "input[placeholder='Password']")            # Change password tag if needed
>>>>>>> 23361caa604fdfd423541970d16f9b977085b42f
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")             # Change login_button tag if needed

    def open_webpage(self, url):
        self.driver.get(url)

    def input_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()