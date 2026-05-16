from helpers import generate_random_credentials
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from url import MAIN_URL, LOGIN_URL
from locators import Registration_Locators, MainPageLocators, Login_Locators
from helpers import generate_random_credentials


class TestRegister:


    def test_register(self, driver):
        
        email, password = generate_random_credentials()

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

            # Заполнение формы
        driver.find_element(*Registration_Locators.NAME_FIELD).send_keys("Елизавета")

        driver.find_element(*Registration_Locators.EMAIL_FIELD).send_keys(email)

        driver.find_element(*Registration_Locators.PASSWORD_FIELD).send_keys(password)

            # Клик по кнопке регистрации
        driver.find_element(*Registration_Locators.REGISTER_BUTTON).click()

            # Проверка, что после успешной регистрации перешли на страницу логина 
        assert WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))


    def test_register_invalid_password(self, driver):
        
        email = generate_random_credentials()

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

            # Заполнение формы
        driver.find_element(*Registration_Locators.NAME_FIELD).send_keys("Елизавета")

        driver.find_element(*Registration_Locators.EMAIL_FIELD).send_keys(email)

        driver.find_element(*Registration_Locators.PASSWORD_FIELD).send_keys("1234")

        # Клик по кнопке регистрации
        driver.find_element(*Registration_Locators.REGISTER_BUTTON).click()

        # Проверка текста ошибки
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Registration_Locators.INCORRECT_PASSWORD_ERROR))


