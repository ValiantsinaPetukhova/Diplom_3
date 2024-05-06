import allure

import data
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = data.Urls.LOGIN_URL
        self.locators = LoginPageLocators()

    @allure.step('Кликаем кнопку восстановления пароля')
    def click_to_recovery_link(self):
        self.click_to_element_with_wait(self.locators.RECOVERY_PASSWORD_LINK)

    @allure.step('Авторизация пользователя')
    def user_login(self, new_user):
        email = new_user['email']
        password = new_user['password']
        self.set_email_field(email)
        self.set_pass_field(password)
        self.login_button_click()

    @allure.step('Заполняем поле email')
    def set_email_field(self, email):
        self.send_text_to_the_element(self.locators.LOGIN_INPUT, email)

    @allure.step('Заполняем поле Пароль')
    def set_pass_field(self, password):
        self.send_text_to_the_element(self.locators.PASSWORD_INPUT, password)

    @allure.step('Кликаем кнопку входа')
    def login_button_click(self):
        self.click_to_element_with_wait(self.locators.LOGIN_BUTTON)

    @allure.step('Проверяем видимость страницы авторизации')
    def check_login_page_is_visible(self):
        return self.check_visibility_of_element(self.locators.LOGIN_PAGE)
