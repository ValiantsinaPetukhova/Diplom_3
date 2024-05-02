import allure

import data
from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = data.Urls.PROFILE_URL
        self.locators = PersonalAccountLocators()

    @allure.step('Проверяем видимость страницы Личный кабинет')
    def check_personal_account_is_visible(self):
        return self.check_visibility_of_element(self.locators.PROFILE_PAGE)

    def click_to_orders_history_button(self):
        self.click_to_element_with_wait(self.locators.ORDERS_HISTORY_BUTTON)

    def click_to_logout_button(self):
        self.click_to_element_with_wait(self.locators.LOGOUT_BUTTON)

