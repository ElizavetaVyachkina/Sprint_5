from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from url import MAIN_URL
from locators import (MainPageLocators)

class TestContructor:

    # Тест перехода в раздел "Булки" 

    def test_navigate_to_buns_section(self, driver):

        driver.get(MAIN_URL)

        driver.find_element(*MainPageLocators.FILLINGS_SECTION).click()

        driver.find_element(*MainPageLocators.BUNS_SECTION).click()

        assert  WebDriverWait(driver, 5).until(EC.presence_of_element_located(MainPageLocators.ACTIVE_BUNS_SECTION))


    # Тест перехода в раздел "Соус" 

    def test_navigate_to_sauces_section(self, driver):

        driver.get(MAIN_URL)

        driver.find_element(*MainPageLocators.SAUCES_SECTION).click()

        assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(MainPageLocators.ACTIVE_SAUCES_SECTION))


# Тест перехода в раздел "Начинки"
    def test_navigate_to_fillings_section(self, driver):

        driver.get(MAIN_URL)

        driver.find_element(*MainPageLocators.FILLINGS_SECTION).click()

        assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(MainPageLocators.ACTIVE_FILLINGS_SECTION))

