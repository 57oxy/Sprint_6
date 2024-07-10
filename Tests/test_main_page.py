import allure
import pytest
from selenium.webdriver.common.by import By
from Page_object.base_page import BasePage
from Page_object.main_page import MainPage
from Confest import driver


@allure.epic('test_samokat_main_page')
class TestMainPage:


    @allure.feature('Test accordion questions')
    @allure.title('Проверка первого вопроса в аккордионе')  # декораторы
    @allure.description('Ищем первый пункт аккордиона и проверяем, что когда нажимаем на стрелочку - открывается соответствующий текст.')
    def test_accordion_1(self, driver):
        # Инициализируем объекты класса
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        # Переходим на страницу ресурса
        base_page.go_to_site()
        # Переходим на первый вопрос
        main_page.find_question_1()
        # Сравниваем текст на странице с тем, что должен быть
        text = main_page.get_question_1_text()
        print(text)
        assert text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Проверка второго вопроса в аккордионе')  # декораторы
    @allure.description('Ищем второй пункт аккордиона и проверяем, что когда нажимаем на стрелочку - открывается соответствующий текст.')
    def test_accordion_2(self, driver):
        # Инициализируем объекты класса
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        # Переходим на страницу ресурса
        base_page.go_to_site()
        # Переходим на второй вопрос
        main_page.find_question_2()
        # Сравниваем текст на странице с тем, что должен быть
        text = main_page.get_question_2_text()
        print(text)
        assert text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('Проверка третьего вопроса в аккордионе')  # декораторы
    @allure.description('Ищем третий пункт аккордиона и проверяем, что когда нажимаем на стрелочку - открывается соответствующий текст.')
    def test_accordion_3(self, driver):
        # Инициализируем объекты класса
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        # Переходим на страницу ресурса
        base_page.go_to_site()
        # Переходим на третий вопрос
        main_page.find_question_3()
        # Сравниваем текст на странице с тем, что должен быть
        text = main_page.get_question_3_text()
        print(text)
        assert text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.title('Проверка четвертого вопроса в аккордионе')  # декораторы
    @allure.description('Ищем четвертый пункт аккордиона и проверяем, что когда нажимаем на стрелочку - открывается соответствующий текст.')
    def test_accordion_4(self, driver):
        # Инициализируем объекты класса
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        # Переходим на страницу ресурса
        base_page.go_to_site()
        # Переходим на четвертый вопрос
        main_page.find_question_4()
        # Сравниваем текст на странице с тем, что должен быть
        text = main_page.get_question_4_text()
        print(text)
        assert text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Проверка пятого вопроса в аккордионе')  # декораторы
    @allure.description('Ищем пятый пункт аккордиона и проверяем, что когда нажимаем на стрелочку - открывается соответствующий текст.')
    def test_accordion_5(self, driver):
        # Инициализируем объекты класса
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        # Переходим на страницу ресурса
        base_page.go_to_site()
        # Переходим на пятый вопрос
        main_page.find_question_5()
        # Сравниваем текст на странице с тем, что должен быть
        text = main_page.get_question_5_text()
        print(text)
        assert text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.title('Проверка шестого вопроса в аккордионе')  # декораторы
    @allure.description('Ищем шестой пункт аккордиона и проверяем, что когда нажимаем на стрелочку - открывается соответствующий текст.')
    def test_accordion_6(self, driver):
        # Инициализируем объекты класса
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        # Переходим на страницу ресурса
        base_page.go_to_site()
        # Переходим на шестой вопрос
        main_page.find_question_6()
        # Сравниваем текст на странице с тем, что должен быть
        text = main_page.get_question_6_text()
        print(text)
        assert text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.title('Проверка седьмого вопроса в аккордионе')  # декораторы
    @allure.description('Ищем седьмой пункт аккордиона и проверяем, что когда нажимаем на стрелочку - открывается соответствующий текст.')
    def test_accordion_7(self, driver):
        # Инициализируем объекты класса
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        # Переходим на страницу ресурса
        base_page.go_to_site()
        # Переходим на седьмой вопрос
        main_page.find_question_7()
        # Сравниваем текст на странице с тем, что должен быть
        text = main_page.get_question_7_text()
        print(text)
        assert text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.title('Проверка восьмого вопроса в аккордионе')  # декораторы
    @allure.description('Ищем восьмой пункт аккордиона и проверяем, что когда нажимаем на стрелочку - открывается соответствующий текст.')
    def test_accordion_8(self, driver):
        # Инициализируем объекты класса
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        # Переходим на страницу ресурса
        base_page.go_to_site()
        # Переходим на восьмой вопрос
        main_page.find_question_8()
        # Сравниваем текст на странице с тем, что должен быть
        text = main_page.get_question_8_text()
        print(text)
        assert text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

