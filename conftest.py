from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from url import LOGIN_URL
from locators import Login_Locators, MainPageLocators
from data import Credentials
from locators import Login_Locators
from data import Credentials
import pytest


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1600,900")
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()

