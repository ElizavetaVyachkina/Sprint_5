from selenium.webdriver.common.by import By

class Registration_Locators:
    # Поле Имя
    NAME_FIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Поле email
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле пароль
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    # Кнопка Зарегистрироваться
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Ошибка некорректного пароля
    INCORRECT_PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")
    # Кнопка входа
    LOGIN_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Войти']")

class PersonalAccountLocators:
    # Кнопка выхода
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    CHEKOUT_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

class Login_Locators:
    # Поле email
    EMAIL_INPUT = (By.XPATH,"//input[@name='name']")
    # Поле пароль
    PASSWORD_INPUT = (By.XPATH,"//input[@type='password']")
    # Кнопка входа
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Кнопка регистрации
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    # Кнопка восстановления пароля
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    # Кнопка "Восстановить"
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")

class MainPageLocators:
    # Кнопка "Войти в аккаунт"
    LOGIN_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")

    # Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")

    # Раздел "Булки"
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")

    # Раздел "Соусы"
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")

    # Раздел "Начинки"
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")

    # Логотип Stellar Burgers
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")

    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")



