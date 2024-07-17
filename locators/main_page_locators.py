from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION_1_CLICK = (By.XPATH, "//div[div[contains(text(), 'Сколько это стоит? И как оплатить?')]]")
    QUESTION_1_PANEL = (By.XPATH, "//div[@id='accordion__panel-0']//p")

    QUESTION_2_CLICK = (By.XPATH, "//div[div[contains(text(), 'Хочу сразу несколько самокатов! Так можно?')]]")
    QUESTION_2_PANEL = (By.XPATH, "//div[@id='accordion__panel-1']//p")

    QUESTION_3_CLICK = (By.XPATH, "//div[div[contains(text(), 'Как рассчитывается время аренды?')]]")
    QUESTION_3_PANEL = (By.XPATH, "//div[@id='accordion__panel-2']//p")

    QUESTION_4_CLICK = (By.XPATH, "//div[div[contains(text(), 'Можно ли заказать самокат прямо на сегодня?')]]")
    QUESTION_4_PANEL = (By.XPATH, "//div[@id='accordion__panel-3']//p")

    QUESTION_5_CLICK = (By.XPATH, "//div[div[contains(text(), 'Можно ли продлить заказ или вернуть самокат раньше?')]]")
    QUESTION_5_PANEL = (By.XPATH, "//div[@id='accordion__panel-4']//p")

    QUESTION_6_CLICK = (By.XPATH, "//div[div[contains(text(), 'Вы привозите зарядку вместе с самокатом?')]]")
    QUESTION_6_PANEL = (By.XPATH, "//div[@id='accordion__panel-5']//p")

    QUESTION_7_CLICK = (By.XPATH, "//div[div[contains(text(), 'Можно ли отменить заказ?')]]")
    QUESTION_7_PANEL = (By.XPATH, "//div[@id='accordion__panel-6']//p")

    QUESTION_8_CLICK = (By.XPATH, "//div[div[contains(text(), 'Я жизу за МКАДом, привезёте?')]]")
    QUESTION_8_PANEL = (By.XPATH, "//div[@id='accordion__panel-7']//p")