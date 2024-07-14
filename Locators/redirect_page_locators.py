from selenium.webdriver.common.by import By


class RedirectPageLocators:

    # Кнопки Заказать
    ORDER_BUTTON_TOP = (By.XPATH, "//div//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    BUTTON_BOTTOM_TEXT = (By.XPATH, "//div[@class='Order_Header__BZXOb']")

    # Тестирование логотипа Самокат
    SAMOKAT_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    SAMOKAT_LOGO_TEXT = (By.XPATH, "//div[@class='Home_SubHeader__zwi_E']")

    # Тестирование логотипа Яндекс
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    YANDEX_LOGO_TEXT = (By.XPATH, "//div[@class='tabs-menu__title-3y tabs-menu__active-1C']")
#'//div[@class='tabs-menu__title-3y tabs-menu__active-1C']'
#"//div[@class='Order_Header__BZXOb']"