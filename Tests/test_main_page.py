import allure
import pytest
from page_object.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from conftest import driver


@allure.epic('test_samokat_main_page')
class TestMainPage:

    @pytest.mark.parametrize('click, panel, verifytext', [
        (MainPageLocators.QUESTION_1_CLICK, MainPageLocators.QUESTION_1_PANEL, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (MainPageLocators.QUESTION_2_CLICK, MainPageLocators.QUESTION_2_PANEL, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        (MainPageLocators.QUESTION_3_CLICK, MainPageLocators.QUESTION_3_PANEL, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (MainPageLocators.QUESTION_4_CLICK, MainPageLocators.QUESTION_4_PANEL, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (MainPageLocators.QUESTION_5_CLICK, MainPageLocators.QUESTION_5_PANEL, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (MainPageLocators.QUESTION_6_CLICK, MainPageLocators.QUESTION_6_PANEL, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (MainPageLocators.QUESTION_7_CLICK, MainPageLocators.QUESTION_7_PANEL, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (MainPageLocators.QUESTION_8_CLICK, MainPageLocators.QUESTION_8_PANEL, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ])
    @allure.feature('Test accordion questions')
    @allure.title('Проверка первого вопросов в аккордионе')  # декораторы
    @allure.description('Ищем пункты аккордиона и проверяем, что когда нажимаем на стрелочку - открывается соответствующий текст.')
    def test_accordion_frases(self, driver, click, panel, verifytext):
        # Инициализируем объекты класса
        main_page = MainPage(driver)
        # Переходим на страницу ресурса
        main_page.go_to_site()
        # Переходим на первый вопрос
        main_page.find_question(click, 17)
        # Сравниваем текст на странице с тем, что должен быть
        text = main_page.get_question_text(panel, 17)
        assert text == verifytext
