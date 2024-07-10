from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Confest import driver

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    # Переходим по ссылке на ресурс
    def go_to_site(self):
        return self.driver.get(self.base_url)