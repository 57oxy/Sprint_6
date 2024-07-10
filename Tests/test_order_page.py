import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Page_object.base_page import BasePage
from Page_object.order_page import OrderPage
from Locators.order_page_locators import OrderPageLocators
from Confest import driver

@allure.epic('test_samokat_main_page')
class TestOrderPage:

    @allure.feature('Test order page functions')
    @allure.title('Тестирование формы регистрации')
    @allure.description('Прогон теста с кнопки "Заказать" сверху, оформление заказа и переход на клавную страницу самоката через логотип.')
    @pytest.mark.parametrize('name, surname, address, metro, phone, date, period, color, comment', [
        ('Тарзан', 'Сергеевич', 'Меченосцев 42', OrderPageLocators.METRO_CASE_1, '81112223344', '12.07.2024', OrderPageLocators.PERIOD_ITEM1, OrderPageLocators.BLACK_COLOR_ITEM, 'Побыстрее, гайз'),
        ('Синдерелла', 'Иванова', 'Ленина 1', OrderPageLocators.METRO_CASE_2, '89051234567', '10.07.2024', OrderPageLocators.PERIOD_ITEM2, OrderPageLocators.GREY_COLOR_ITEM, 'Продам гараж')
    ])
    def test_case_1(self, driver, name, surname, address, metro, phone, date, period, color, comment):
        # Инициализируем объекты класса
        base_page = BasePage(driver)
        order_page = OrderPage(driver)
        # Переходим на страницу ресурса
        base_page.go_to_site()
        # Кликаем на верхнюю кнопку Заказать сверху
        order_page.Order_button_top_click()
        # Заполняем поле Имя
        order_page.Fill_name_field(name)
        # Заполняем поле Фамилия
        order_page.Fill_surname_field(surname)
        # Заполняем поле Адрес
        order_page.Fill_address_field(address)
        # Заполняем поле Метро
        order_page.Fill_metro_field(metro)
        # Заполняем поле Телефон
        order_page.Fill_phone_field(phone)
        # Нажимаем кнопку Далее
        order_page.Next_button_click()
        # Заполняем поле Дата доставки
        order_page.Fill_date_field(date)
        # Заполняем поле На сколько арендуем
        order_page.Fill_period_field(period)
        # Выбираем цвет
        order_page.Fill_color_field(color)
        # Заполняем поле Комментарий
        order_page.Fill_comment_field(comment)
        # Жмем кнопку Заказать
        order_page.Order_button_click()
        # Подтверждаем заказ
        order_page.Confirm_order()
        # Сравниваем текст в поле созданного заказа, там должна быть строка Номер заказа
        order_text = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((OrderPageLocators.ORDER_TEXT))).text
        print(order_text)
        assert 'Номер заказа' in order_text

    @allure.title('Тестирование нижней кнопки "Заказать"')
    @allure.description('Нажимаем кнопку "Заказать" снизу и проверяем, что попали в форму оформления заказа')
    def test_bottom_order_button(self, driver):
        # Инициализируем объекты класса
        base_page = BasePage(driver)
        order_page = OrderPage(driver)
        # Переходим на страницу ресурса
        base_page.go_to_site()
        # Кликаем на верхнюю кнопку Заказать снизу
        order_page.Order_button_bottom_click()
        # Сравниваем текст на странице оформления заказа должна быть строка Для кого самокат
        text = WebDriverWait(driver, 15).until(ec.visibility_of_element_located((OrderPageLocators.BUTTON_BOTTOM_TEXT))).text
        assert text == 'Для кого самокат'

    @allure.title('Проверка логотипа Самокат')
    @allure.description('Проверка работы логотипа Самокат, что он переходит на главную страницу Самокат')
    def test_logo_samokat(self, driver):
        # Инициализируем объекты класса
        base_page = BasePage(driver)
        order_page = OrderPage(driver)
        # Переходим на страницу ресурса
        base_page.go_to_site()
        # Кликаем на верхнюю кнопку Заказать сверху чтобы перейти с главной страницы
        order_page.Order_button_top_click()
        # Кликаем на логотип Самокат
        order_page.Samokat_logo_click()
        # Сравниваем текст на странице, там должна быть строка Привезём его прямо к вашей двери
        text = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((OrderPageLocators.SAMOKAT_LOGO_TEXT))).text
        assert 'Привезём его прямо к вашей двери' in text

    @allure.title('Проверка логотипа Яндекс')
    @allure.description('Проверка работы логотипа Яндекс, что он переходит на главную страницу Яндекс')
    def test_logo_yandex(self, driver):
        # Инициализируем объекты класса
        base_page = BasePage(driver)
        order_page = OrderPage(driver)
        # Переходим на страницу ресурса
        base_page.go_to_site()
        # Кликаем на логотип Самокат
        order_page.Yandex_logo_click()
        # Создаем переменную с значением следующей открытой вкладки
        window_after = driver.window_handles[1]
        # Переходим на следующую вкладку
        driver.switch_to.window(window_after)
        # Сравниваем текст на странице, там должна быть кнопка с текстом Главное
        text = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((OrderPageLocators.YANDEX_LOGO_TEXT))).text
        assert text == 'Главное'