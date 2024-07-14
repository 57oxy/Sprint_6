from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from conftest import driver


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    # Переходим по ссылке на ресурс
    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element_located(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(ec.visibility_of_element_located(locator), message=f'Not found {locator}')
