import allure

import data
from locators.recovery_page_locators import RecoveryPageLocators
from pages.base_page import BasePage


class RecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = data.Urls.RECOVER_URL
        self.locators = RecoveryPageLocators()

    @allure.step('Проверяем видимость страницы восстановления')
    def check_recovery_page_is_visible(self):
        return self.check_visibility_of_element(self.locators.RECOVERY_PASSWORD_PAGE)

    @allure.step('Заполняем поле email')
    def fill_in_email_field(self, new_user):
        email = new_user["email"]
        self.send_text_to_the_element(self.locators.RECOVERY_EMAIL_INPUT, email)

    @allure.step('Получаем значение поля email')
    def get_email(self):
        return self.get_value_from_element(self.locators.RECOVERY_EMAIL_INPUT)

    @allure.step('Клик по кнопке Восстановить')
    def click_to_recovery_button(self):
        self.click_to_element_with_wait(self.locators.RECOVERY_BUTTON)

    @allure.step('Кликаем на глаз в поле восстановления пароля')
    def click_to_eye_button(self):
        self.click_to_element_with_wait(self.locators.RECOVERY_EYE_PASSWORD)

    @allure.step('получаем назнание класса')
    def get_eye_class_name(self):
        return self.get_class_name(self.locators.RECOVERY_PASSWORD_INPUT)

    @allure.step('Ждем загрузки страницы восстановления пароля')
    def wait_recovery_page(self):
        self.wait_element_is_visible(self.locators.RECOVERY_SET_PASSWORD_PAGE)


