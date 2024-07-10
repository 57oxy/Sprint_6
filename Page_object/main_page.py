import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Page_object.base_page import BasePage
from Locators.main_page_locators import MainPageLocators
from Confest import driver

class MainPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищем первый элемент аккордеона и кликаем по нему, чтобы появился текст ответа на вопрос')  # декоратор
    def find_question_1(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_1_CLICK)))
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_1_CLICK))).click()

    @allure.step('Получаем текст ответа на вопрос для сравнения')  # декоратор
    def get_question_1_text(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_1_PANEL)))
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_1_PANEL))).text

    def find_question_2(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_3_CLICK)))
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_2_CLICK))).click()

    def get_question_2_text(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_2_PANEL)))
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_2_PANEL))).text

    def find_question_3(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_3_CLICK)))
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_3_CLICK))).click()

    def get_question_3_text(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_3_PANEL)))
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_3_PANEL))).text

    def find_question_4(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_4_CLICK)))
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_4_CLICK))).click()

    def get_question_4_text(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_4_PANEL)))
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_4_PANEL))).text

    def find_question_5(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_5_CLICK)))
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_5_CLICK))).click()

    def get_question_5_text(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_5_PANEL)))
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_5_PANEL))).text

    def find_question_6(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_6_CLICK)))
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_6_CLICK))).click()

    def get_question_6_text(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_6_PANEL)))
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_6_PANEL))).text

    def find_question_7(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_7_CLICK)))
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_7_CLICK))).click()

    def get_question_7_text(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_7_PANEL)))
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_7_PANEL))).text

    def find_question_8(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_8_CLICK)))
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_8_CLICK))).click()

    def get_question_8_text(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_8_PANEL)))
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((MainPageLocators.QUESTION_8_PANEL))).text