from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    LOGOUT_BUTTON = By.XPATH, ".//button[text()='Выход']"  # кнопка выхода из аккаунта
    PROFILE_PAGE = By.LINK_TEXT, "Профиль"  # страница профиля
    ORDERS_HISTORY_BUTTON = By.XPATH, './/a[text()="История заказов"]'

