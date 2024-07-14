import allure
import pytest
from page_object.base_page import BasePage
from locators.redirect_page_locators import RedirectPageLocators
from conftest import driver

class RedirectPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"
    def go_to_site(self):
        return self.driver.get(self.base_url)

    @allure.step('Ищем элемент на странице')
    def find_element(self, locator, time):
        return super().find_element_located(locator, time)

    @allure.step('Ищем сверху кнопку "Заказать" и нажимаем ее')  # декоратор
    def order_button_top_click(self):
        super().find_element_located(RedirectPageLocators.ORDER_BUTTON_TOP, 10).click()

    @allure.step('Нажимаем на логотип "Самокат"')
    def samokat_logo_click(self):
        super().find_element_located(RedirectPageLocators.SAMOKAT_LOGO, 10).click()

    @allure.step('Нажимаем на логотип "Яндекс"')
    def yandex_logo_click(self):
        super().find_element_located(RedirectPageLocators.YANDEX_LOGO, 15).click()
