from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    RECOVERY_PASSWORD_PAGE = By.XPATH, ".//h2[text()='Восстановление пароля']"
    RECOVERY_EMAIL_INPUT = By.XPATH, '//input[@name="name"]'
    RECOVERY_BUTTON = By.XPATH, ".//button[text()='Восстановить']"
    RECOVERY_SET_PASSWORD_PAGE = By.XPATH, "//label[text() ='Введите код из письма']"
    RECOVERY_EYE_PASSWORD = By.CLASS_NAME, 'input__icon'
    RECOVERY_PASSWORD_INPUT = By.XPATH, './/label[text()="Пароль"]'

