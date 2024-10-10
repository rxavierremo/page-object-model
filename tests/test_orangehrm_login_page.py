import pytest
import time
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    # driver.quit()

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_webpage("https://opensource-demo.orangehrmlive.com/")
    time.sleep(1)
    login_page.input_username("Admin")
    time.sleep(1)
    login_page.input_password("admin123")
    time.sleep(1)
    login_page.click_login()
    time.sleep(5)



