from selenium.webdriver.common.by import By


class LoginPageLocators:
    RECOVERY_PASSWORD_LINK = By.LINK_TEXT, "Восстановить пароль"
    LOGIN_PAGE = By.XPATH, "//h2[text()='Вход']"   # страница входа
    LOGIN_INPUT = By.XPATH, ".//label[text()='Email']/following-sibling::input[@type='text']"  # поле ввода логина на странице входа
    PASSWORD_INPUT = By.XPATH, ".//label[text()='Пароль']/following-sibling::input[@type='password']"  # поле ввода пароля на странице входа
    LOGIN_BUTTON = By.XPATH, ".//button[text()='Войти']"  # кнопка Войти
