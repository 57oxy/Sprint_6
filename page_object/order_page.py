import allure
from page_object.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):


    @allure.step('Заходим на сайт')
    def go_to_site(self):
        return super().go_to_site()

    @allure.step('Ищем сверху кнопку "Заказать" и нажимаем ее')  # декоратор
    def order_button_top_click(self):
        super().find_element_located(OrderPageLocators.ORDER_BUTTON_TOP, 10).click()

    @allure.step('Ищем внизу кнопку "Заказать" и нажимаем ее')  # декоратор
    def order_button_bottom_click(self):
        element = super().find_element_located(OrderPageLocators.ORDER_BUTTON_BOTTOM, 15)
        super().scroll_to_element(element)
        super().find_element_located(OrderPageLocators.ORDER_BUTTON_BOTTOM, 10).click()

    @allure.step('Заполняем поле "Имя"')
    def fill_name_field(self, name):
        search_field = super().find_element_located(OrderPageLocators.NAME_FIELD,15)
        search_field.send_keys(name)
        return search_field

    @allure.step('Заполняем поле "Фамилия"')
    def fill_surname_field(self, surname):
        search_field = super().find_element_located(OrderPageLocators.SURNAME_FIELD, 15)
        search_field.send_keys(surname)
        return search_field

    @allure.step('Заполняем поле "Адрес"')
    def fill_address_field(self, address):
        search_field = super().find_element_located(OrderPageLocators.ADDRESS_FIELD, 15)
        search_field.send_keys(address)
        return search_field

    @allure.step('Заполняем поле "Метро"')
    def fill_metro_field(self, metro):
        super().find_element_located(OrderPageLocators.METRO_FIELD, 15).click()
        search_field = super().find_element_located(metro, 15)
        search_field.click()
        return search_field

    @allure.step('Заполняем поле "Номер телефона"')
    def fill_phone_field(self, phone):
        search_field = super().find_element_located(OrderPageLocators.PHONE_FIELD, 15)
        search_field.send_keys(phone)
        return search_field

    @allure.step('Кликаем по кнопке "Далее"')
    def next_button_click(self):
        super().find_element_located(OrderPageLocators.COOKIE_BUTTON, 15).click()
        super().find_element_located(OrderPageLocators.NEXT_BUTTON, 15).click()

    @allure.step('Кликаем по кнопке "Заказать"')
    def order_button_click(self):
        super().find_element_located(OrderPageLocators.NEXT_BUTTON, 15).click()

    @allure.step('Заполняем поле "Дата доставки"')
    def fill_date_field(self, date):
        search_field = super().find_element_located(OrderPageLocators.DATE_FIELD, 15)
        search_field.send_keys(date)
        return search_field

    @allure.step('Заполняем поле "Период доставки"')
    def fill_period_field(self, period):
        super().find_element_located(OrderPageLocators.PERIOD_FIELD, 15).click()
        search_field = super().find_element_located(period, 15)
        search_field.click()
        return search_field

    @allure.step('Заполняем поле "Цвет"')
    def fill_color_field(self, color):
        search_field = super().find_element_located(color, 15)
        search_field.click()
        return search_field

    @allure.step('Заполняем поле "Комментарий"')
    def fill_comment_field(self, comment):
        search_field = super().find_element_located(OrderPageLocators.COMMENT_FIELD, 15)
        search_field.send_keys(comment)
        return search_field

    @allure.step('Подтверждаем заказ кнопкой "Да"')
    def confirm_order(self):
        super().find_element_located(OrderPageLocators.CONFIRM_BUTTON, 15).click()

    @allure.step('Ищем элемент на странице')
    def find_element(self, locator, time):
        return super().find_element_located(locator, time)

    def find_order_text(self):
        return super().find_element_located(OrderPageLocators.ORDER_TEXT, 15).text

    def find_yandex_logo_text(self):
        return super().find_element_located(OrderPageLocators.YANDEX_LOGO_TEXT, 15).text






