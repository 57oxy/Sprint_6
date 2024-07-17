import allure
from page_object.base_page import BasePage
from locators.redirect_page_locators import RedirectPageLocators


class RedirectPage(BasePage):

    def go_to_site(self):
        return super().go_to_site()

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

    def find_samokat_logo_text(self):
        return super().find_element_located(RedirectPageLocators.SAMOKAT_LOGO_TEXT, 15).text

    def find_yandex_logo_text(self):
        return super().find_element_located(RedirectPageLocators.YANDEX_LOGO_TEXT, 10).text

    def switch_to_next_tab(self):
        # Создаем переменную с значением следующей открытой вкладки
        window_after = self.driver.window_handles[1]
        # Переходим на следующую вкладку
        return self.driver.switch_to.window(window_after)