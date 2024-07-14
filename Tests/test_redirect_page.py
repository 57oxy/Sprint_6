import allure
import pytest
from page_object.redirect_page import RedirectPage
from locators.redirect_page_locators import RedirectPageLocators
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
        text = redirect_page.find_element(RedirectPageLocators.SAMOKAT_LOGO_TEXT, 15).text
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
        # Создаем переменную с значением следующей открытой вкладки
        window_after = driver.window_handles[1]
        # Переходим на следующую вкладку
        driver.switch_to.window(window_after)
        # Сравниваем текст на странице, там должна быть кнопка с текстом Главное
        text = redirect_page.find_element(RedirectPageLocators.YANDEX_LOGO_TEXT, 10).text
        assert text == 'Главное'
