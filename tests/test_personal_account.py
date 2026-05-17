from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from url import MAIN_URL, PROFILE_URL
from locators import (
    MainPageLocators,
    Login_Locators,
    PersonalAccountLocators
)
from data import Credentials
from helpers import login_user

class TestPersonalAccount:

    # Тест на переход по клику в «Личный кабинет».
    def test_personal_account(self, driver):

        driver.get(MAIN_URL)

        # Клик по кнопке "Войти в аккаунт"
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        # Ожидание страницы логина
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.LOGIN_SUBMIT_BUTTON))

        login_user(driver)

        # Клик по кнопке "Личный кабинет"
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Проверка URL
        assert WebDriverWait(driver, 10).until(EC.url_to_be(PROFILE_URL))

    # Тест на переход из личного кабинета в конструктор 
    def test_navigate_to_constructor_from_account(self, driver):
        
        driver.get(MAIN_URL)

        # Клик по кнопке "Войти в аккаунт"
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        # Ожидание страницы логина
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.LOGIN_SUBMIT_BUTTON))

        login_user(driver)
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_contains(PROFILE_URL))

        # Клик по кнопке "Конструктор"
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersonalAccountLocators.CHEKOUT_BUTTON))

    

    # Тест переход из личного кабинета клик на логотип Stellar Burgers.
    def test_logo_click_from_account(self, driver):
        
        driver.get(MAIN_URL)

        # Клик по кнопке "Войти в аккаунт"
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        # Ожидание страницы логина
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.LOGIN_SUBMIT_BUTTON))

        login_user(driver)
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_contains(PROFILE_URL))

        # Клик по логотипу "Stellar Burgers"
        driver.find_element(*MainPageLocators.LOGO).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersonalAccountLocators.CHEKOUT_BUTTON))

    # Тест на выход из аккаунта по кнопке «Выйти» в личном кабинете.
    def test_logout(self, driver):

        driver.get(MAIN_URL)

        # Клик по кнопке "Войти в аккаунт"
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        # Ожидание страницы логина
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.LOGIN_SUBMIT_BUTTON))

        login_user(driver)
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_contains(PROFILE_URL))

        driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.LOGIN_SUBMIT_BUTTON))

