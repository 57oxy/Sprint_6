from selenium.webdriver.common.by import By


class OrderPageLocators:

    # Кнопки Заказать
    ORDER_BUTTON_TOP = (By.XPATH, "//div//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    BUTTON_BOTTOM_TEXT = (By.XPATH, "//div[@class='Order_Header__BZXOb']")

    # Форма регистрации первая страница
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_CASE_1 = (By.XPATH, "//div[text()='Черкизовская']")
    METRO_CASE_2 = (By.XPATH, "//div[text()='Сокольники']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # Кнопка Назад и Куки, чтобы открыть кнопку Назад
    COOKIE_BUTTON = (By.XPATH, "//button[@id='rcc-confirm-button']")
    NEXT_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

    # Форма регистрации вторая страница
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    PERIOD_FIELD = (By.XPATH, "//span[@class='Dropdown-arrow']")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    CONFIRM_BUTTON = (By.XPATH, "//div//button[contains(text(), 'Да')]")

    # Переменные для параметризации и подтвержждение заказа
    ORDER_SUCCESS = (By.XPATH, "/div[@class='Order_ModalHeader__3FDaJ']")
    ORDER_TEXT = (By.XPATH, "//div[@class='Order_Text__2broi']")
    PERIOD_ITEM1 = (By.XPATH, "//div[@class='Dropdown-menu']//div[2]")
    PERIOD_ITEM2 = (By.XPATH, "//div[@class='Dropdown-menu']//div[3]")
    BLACK_COLOR_ITEM = (By.XPATH, "//input[@id='black']")
    GREY_COLOR_ITEM = (By.XPATH, "//input[@id='grey']")

    YANDEX_LOGO_TEXT = (By.XPATH, "//div[@class='Order_Header__BZXOb']")
