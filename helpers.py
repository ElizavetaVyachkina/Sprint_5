from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Login_Locators
from data import Credentials
from url import MAIN_URL


faker = Faker()


def generate_random_credentials():
    email = faker.email()
    password = faker.password(length=10, special_chars=True, digits=True)
    return email, password


def login_user(driver):
    
    # Вводим email и пароль
    driver.find_element(*Login_Locators.EMAIL_INPUT).send_keys(Credentials.email)
    driver.find_element(*Login_Locators.PASSWORD_INPUT).send_keys(Credentials.password)
    
    # Кликаем по кнопке Вход
    driver.find_element(*Login_Locators.LOGIN_SUBMIT_BUTTON).click()

    # Ожидаем успешную авторизацию (попадание на главную страницу)
    WebDriverWait(driver, 10).until(EC.url_contains(MAIN_URL))

