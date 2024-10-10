import pytest
<<<<<<< HEAD
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage
=======
from login_page import LoginPage
import time
from selenium import webdriver
>>>>>>> 23361caa604fdfd423541970d16f9b977085b42f

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
<<<<<<< HEAD
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    # driver.quit()
=======
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()
>>>>>>> 23361caa604fdfd423541970d16f9b977085b42f

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_webpage("https://opensource-demo.orangehrmlive.com/")
    time.sleep(1)
    login_page.input_username("Admin")
    time.sleep(1)
    login_page.input_password("admin123")
    time.sleep(1)
    login_page.click_login()
<<<<<<< HEAD
    time.sleep(1)

    assert "Successful" in driver.page_source
    time.sleep(1)







=======
    time.sleep(1)
>>>>>>> 23361caa604fdfd423541970d16f9b977085b42f
