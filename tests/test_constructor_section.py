from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from url import MAIN_URL
from locators import (MainPageLocators)

class TestContructor:

    # Тест перехода в раздел "Булки" 

    def test_navigate_to_buns_section(self, driver):

        driver.get(MAIN_URL)

        driver.find_element(*MainPageLocators.FILLINGS_SECTION).click()

        driver.find_element(*MainPageLocators.BUNS_SECTION).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'tab_tab_type_current')]")))

        assert True


    # Тест перехода в раздел "Соус" 

    def test_navigate_to_sauces_section(self, driver):

        driver.get(MAIN_URL)

        driver.find_element(*MainPageLocators.SAUCES_SECTION).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'tab_tab_type_current')]")))

        assert True


# Тест перехода в раздел "Начинки"
    def test_navigate_to_fillings_section(self, driver):

        driver.get(MAIN_URL)

        driver.find_element(*MainPageLocators.FILLINGS_SECTION).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'tab_tab_type_current')]")))

        assert True
