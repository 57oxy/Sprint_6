import allure
import pytest
from page_object.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from conftest import driver


@allure.epic('test_samokat_main_page')
class TestOrderPage:

    @allure.feature('Test order page functions')
    @allure.title('Тестирование формы регистрации')
    @allure.description('Прогон теста с кнопки "Заказать" сверху, оформление заказа и переход на клавную страницу самоката через логотип.')
    @pytest.mark.parametrize('name, surname, address, metro, phone, date, period, color, comment', [
        ('Тарзан', 'Сергеевич', 'Меченосцев 42', OrderPageLocators.METRO_CASE_1, '81112223344', '12.07.2024', OrderPageLocators.PERIOD_ITEM1, OrderPageLocators.BLACK_COLOR_ITEM, 'Побыстрее, гайз'),
        ('Синдерелла', 'Иванова', 'Ленина 1', OrderPageLocators.METRO_CASE_2, '89051234567', '10.07.2024', OrderPageLocators.PERIOD_ITEM2, OrderPageLocators.GREY_COLOR_ITEM, 'Продам гараж')
    ])
    def test_order_function(self, driver, name, surname, address, metro, phone, date, period, color, comment):
        # Инициализируем объекты класса
        order_page = OrderPage(driver)
        # Переходим на страницу ресурса
        order_page.go_to_site()
        # Кликаем на верхнюю кнопку Заказать сверху
        order_page.order_button_top_click()
        # Заполняем поле Имя
        order_page.fill_name_field(name)
        # Заполняем поле Фамилия
        order_page.fill_surname_field(surname)
        # Заполняем поле Адрес
        order_page.fill_address_field(address)
        # Заполняем поле Метро
        order_page.fill_metro_field(metro)
        # Заполняем поле Телефон
        order_page.fill_phone_field(phone)
        # Нажимаем кнопку Далее
        order_page.next_button_click()
        # Заполняем поле Дата доставки
        order_page.fill_date_field(date)
        # Заполняем поле На сколько арендуем
        order_page.fill_period_field(period)
        # Выбираем цвет
        order_page.fill_color_field(color)
        # Заполняем поле Комментарий
        order_page.fill_comment_field(comment)
        # Жмем кнопку Заказать
        order_page.order_button_click()
        # Подтверждаем заказ
        order_page.confirm_order()
        # Сравниваем текст в поле созданного заказа, там должна быть строка Номер заказа
        order_text = order_page.find_order_text()
        assert 'Номер заказа' in order_text

    @allure.title('Тестирование нижней кнопки "Заказать"')
    @allure.description('Нажимаем кнопку "Заказать" снизу и проверяем, что попали в форму оформления заказа')
    def test_bottom_order_button(self, driver):
        # Инициализируем объекты класса
        order_page = OrderPage(driver)
        # Переходим на страницу ресурса
        order_page.go_to_site()
        # Кликаем на верхнюю кнопку Заказать снизу
        order_page.order_button_bottom_click()
        # Сравниваем текст на странице оформления заказа должна быть строка Для кого самокат
        yandex_logo_text = order_page.find_yandex_logo_text()
        assert yandex_logo_text == 'Для кого самокат'
