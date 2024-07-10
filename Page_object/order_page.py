import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from Page_object.base_page import BasePage
from Locators.order_page_locators import OrderPageLocators
from Confest import driver

class OrderPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищем сверху кнопку "Заказать" и нажимаем ее')  # декоратор
    def Order_button_top_click(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((OrderPageLocators.ORDER_BUTTON_TOP))).click()

    @allure.step('Ищем cнизу кнопку "Заказать" и нажимаем ее')  # декоратор
    def Order_button_bottom_click(self):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((OrderPageLocators.ORDER_BUTTON_BOTTOM)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((OrderPageLocators.ORDER_BUTTON_BOTTOM))).click()

    @allure.step('Заполняем поле "Имя"')
    def Fill_name_field(self, name):
        search_field = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((OrderPageLocators.NAME_FIELD)))
        search_field.send_keys(name)
        return search_field

    @allure.step('Заполняем поле "Фамилия"')
    def Fill_surname_field(self, surname):
        search_field = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((OrderPageLocators.SURNAME_FIELD)))
        search_field.send_keys(surname)
        return search_field

    @allure.step('Заполняем поле "Адрес"')
    def Fill_address_field(self, address):
        search_field = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((OrderPageLocators.ADDRESS_FIELD)))
        search_field.send_keys(address)
        return search_field

    @allure.step('Заполняем поле "Метро"')
    def Fill_metro_field(self, metro):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((OrderPageLocators.METRO_FIELD))).click()
        search_field = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((metro)))
        search_field.click()
        return search_field

    @allure.step('Заполняем поле "Номер телефона"')
    def Fill_phone_field(self, phone):
        search_field = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((OrderPageLocators.PHONE_FIELD)))
        search_field.send_keys(phone)
        return search_field

    @allure.step('Кликаем по кнопке "Далее"')
    def Next_button_click(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((OrderPageLocators.COOKIE_BUTTON))).click()
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((OrderPageLocators.NEXT_BUTTON))).click()

    @allure.step('Кликаем по кнопке "Заказать"')
    def Order_button_click(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((OrderPageLocators.NEXT_BUTTON))).click()

    @allure.step('Заполняем поле "Дата доставки"')
    def Fill_date_field(self, date):
        search_field = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((OrderPageLocators.DATE_FIELD)))
        search_field.send_keys(date)
        return search_field

    @allure.step('Заполняем поле "Период доставки"')
    def Fill_period_field(self, period):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((OrderPageLocators.PERIOD_FIELD))).click()
        search_field = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((period)))
        search_field.click()
        return search_field

    @allure.step('Заполняем поле "Цвет"')
    def Fill_color_field(self, color):
        search_field = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((color)))
        search_field.click()
        return search_field

    @allure.step('Заполняем поле "Комментарий"')
    def Fill_comment_field(self, comment):
        search_field = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((OrderPageLocators.COMMENT_FIELD)))
        search_field.send_keys(comment)
        return search_field

    @allure.step('Подтверждаем заказ кнопкой "Да"')
    def Confirm_order(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((OrderPageLocators.CONFIRM_BUTTON))).click()

    @allure.step('Нажимаем на логотип "Самокат"')
    def Samokat_logo_click(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((OrderPageLocators.SAMOKAT_LOGO))).click()

    @allure.step('Нажимаем на логотип "Яндекс"')
    def Yandex_logo_click(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((OrderPageLocators.YANDEX_LOGO))).click()






