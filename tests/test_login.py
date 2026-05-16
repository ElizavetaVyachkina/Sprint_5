from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from url import MAIN_URL, LOGIN_URL, PROFILE_URL
from locators import (
    MainPageLocators,
    Login_Locators,
    Registration_Locators,
)
from helpers import login_user

class TestLogin:

    # Тест №1: Вход через кнопку "Войти в аккаунт" на главной
    def test_login_from_main_page(self, driver):

        # Открыть главную страницу
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

    # Тест №2: Вход через кнопку "Личный кабинет"
    def test_login_from_personal_account_button(self, driver):

        # Переходим на главную
        driver.get(MAIN_URL)
    
        # Кликаем по кнопке "Личный кабинет"
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    
        # Проверяем, что попали на форму входа
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
    
        # Вводим email и пароль
        login_user(driver)

        # Клик по кнопке "Личный кабинет"
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        assert WebDriverWait(driver, 10).until(EC.url_to_be(PROFILE_URL))

    # Тест №3: Вход через кнопку "Войти" на форме регистрации
    def test_login_from_registration_form(self, driver):
    
        # Открыть главную страницу
        driver.get(MAIN_URL)

        # Клик по кнопке "Войти в аккаунт"
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        # Ожидание страницы логина
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.LOGIN_SUBMIT_BUTTON))

        # Переход на страницу регистрации
        driver.find_element(*Login_Locators.REGISTER_LINK).click()

        # Ожидание формы регистрации
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                Registration_Locators.REGISTER_BUTTON
            )
        )

        driver.find_element(*Registration_Locators.LOGIN_LINK).click()

        # Проверяем, что попали на форму входа
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))

        login_user(driver)

        # Клик по кнопке "Личный кабинет"
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        assert WebDriverWait(driver, 10).until(EC.url_to_be(PROFILE_URL))

        

    # Тест №4: Вход через кнопку "Войти" на форме восстановления пароля
    def test_login_from_forgot_password_form(self, driver):
   
        # Переходим на страницу логина и кликаем на "Восстановить пароль"
        driver.get(LOGIN_URL)
        driver.find_element(*Login_Locators.FORGOT_PASSWORD_LINK).click()

    
        # Кликаем по ссылке "Войти"
        driver.find_element(*Registration_Locators.LOGIN_LINK).click()
    
        # Проверяем, что попали на форму входа
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.FORGOT_PASSWORD_BUTTON))

        login_user(driver)

        # Клик по кнопке "Личный кабинет"
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        assert WebDriverWait(driver, 10).until(EC.url_to_be(PROFILE_URL))

        