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

    def scroll_to_body(self):
        return self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def scroll_to_element(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def move_to_next_tab(self):
        # Создаем переменную с значением следующей открытой вкладки
        window_after = self.driver.window_handles[1]
        # Переходим на следующую вкладку
        return self.driver.switch_to.window(window_after)