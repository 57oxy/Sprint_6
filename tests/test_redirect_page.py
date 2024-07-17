import allure
import pytest
from page_object.redirect_page import RedirectPage
from conftest import driver


@allure.epic('test_samokat_main_page')
class TestRedirectPage:

    @allure.title('Проверка логотипа Самокат')
    @allure.description('Проверка работы логотипа Самокат, что он переходит на главную страницу Самокат')
    def test_logo_samokat(self, driver):
        # Инициализируем объекты класса
        redirect_page = RedirectPage(driver)
        # Переходим на страницу ресурса
        redirect_page.go_to_site()
        # Кликаем на верхнюю кнопку Заказать сверху, чтобы перейти с главной страницы
        redirect_page.order_button_top_click()
        # Кликаем на логотип Самокат
        redirect_page.samokat_logo_click()
        # Сравниваем текст на странице, там должна быть строка Привезём его прямо к вашей двери
        text = redirect_page.find_samokat_logo_text()
        assert 'Привезём его прямо к вашей двери' in text

    @allure.title('Проверка логотипа Яндекс')
    @allure.description('Проверка работы логотипа Яндекс, что он переходит на главную страницу Яндекс')
    def test_logo_yandex(self, driver):
        # Инициализируем объекты класса
        redirect_page = RedirectPage(driver)
        # Переходим на страницу ресурса
        redirect_page.go_to_site()
        # Кликаем на логотип Самокат
        redirect_page.yandex_logo_click()
        # Переходим на следующую вкладку
        redirect_page.switch_to_next_tab()
        # Сравниваем текст на странице, там должна быть кнопка с текстом Главное
        text = redirect_page.find_yandex_logo_text()
        assert text == 'Главное'
