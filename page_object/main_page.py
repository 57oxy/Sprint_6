import allure
from page_object.base_page import BasePage

class MainPage(BasePage):


    @allure.step('Заходим на сайт')
    def go_to_site(self):
        return super().go_to_site()

    @allure.step('Ищем элемент аккордеона и кликаем по нему, чтобы появился текст ответа на вопрос')  # декоратор
    def find_question(self, locator, time):
        super().find_element_located(locator, time)
        super().scroll_to_body()
        super().find_element_located(locator, time).click()

    @allure.step('Получаем текст ответа на вопрос для сравнения')  # декоратор
    def get_question_text(self, locator, time):
        super().find_element_located(locator, time)
        return super().find_element_located(locator, time).text
