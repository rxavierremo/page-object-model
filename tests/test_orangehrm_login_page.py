import pytest

from login_page import LoginPage
import time
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_webpage("https://opensource-demo.orangehrmlive.com/")
    time.sleep(1)
    login_page.input_username("Admin")
    time.sleep(1)
    login_page.input_password("admin123")
    time.sleep(1)
    login_page.click_login()
