from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_ACCOUNT_BUTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"  # кнопка "Войти в аккаунт" на главной странице
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, ".//a[contains(., 'Личный Кабинет')]"  # кнопка Личный кабинет
    MAIN_PAGE = By.XPATH, "//h1[text()='Соберите бургер']"  # главная страница
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text()='Конструктор']"
    ORDERS_FEED_BUTTON = By.XPATH, "//p[text()='Лента Заказов']"
    INGREDIENT_LOCATOR = By.XPATH, "//a[@href='/ingredient/{}']"
    INGREDIENT_DETAILS = By.XPATH, "//h2[text()='Детали ингредиента']"
    INGRIDIENT_DETAILS_CLOSE = By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS"
    BUCKET = By.XPATH, ".//ul[contains(@class,'BurgerConstructor_basket')]"
    BUCKET_COUNTER = By.CSS_SELECTOR, ".text.text_type_digits-medium"
    INGREDIENT_COUNTER = By.XPATH, "//p[contains(@class, 'counter__num')]"
    DEFAULT_ORDER_NUMBER = By.XPATH, "//div/h2[text()='9999']"
    ORDER_COMPLETE_BOX = By.XPATH, "//p[text()='идентификатор заказа']"
    ORDER_BUTTON = By.XPATH, ".//button[text()='Оформить заказ']"
    ORDER_NUMBER = By.XPATH, "//h2[contains(@class,'Modal_modal__title_shadow')]"
    CROSS_BUTTON = By.XPATH, ".//button[@type='button']"

