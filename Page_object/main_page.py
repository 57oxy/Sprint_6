import allure
import pytest
from page_object.base_page import BasePage
from conftest import driver

class MainPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    @allure.step('Заходим на сайт')
    def go_to_site(self):
        return self.driver.get(self.base_url)

    @allure.step('Ищем элемент аккордеона и кликаем по нему, чтобы появился текст ответа на вопрос')  # декоратор
    def find_question(self, locator, time):
        super().find_element_located(locator, time)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        super().find_element_located(locator, time).click()

    @allure.step('Получаем текст ответа на вопрос для сравнения')  # декоратор
    def get_question_text(self, locator, time):
        super().find_element_located(locator, time)
        return super().find_element_located(locator, time).text
