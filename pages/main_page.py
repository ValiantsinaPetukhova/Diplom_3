import allure

import data
from helpers import GenerateTestData
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = data.Urls.BASE_URL
        self.locators = MainPageLocators()

    @allure.step('Кликаем кнопку личного кабинета')
    def click_to_personal_account_button(self):
        self.click_to_element_with_wait(self.locators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Кликаем кнопку конструктора')
    def click_to_constructor_button(self):
        self.click_to_element_with_wait(self.locators.CONSTRUCTOR_BUTTON)

    @allure.step('Проверяем видимость страницы с конструктором')
    def check_constructor_page_is_visible(self):
        return self.check_visibility_of_element(self.locators.MAIN_PAGE)

    @allure.step('Кликаем на кнопку лента заказов')
    def click_to_orders_feed_button(self):
        self.click_to_element_with_wait(self.locators.ORDERS_FEED_BUTTON)

    @allure.step('Кликаем на ингредиент')
    def click_to_ingredient(self, ingredient):
        locator_formatted = self.format_locators(self.locators.INGREDIENT_LOCATOR, ingredient)
        self.click_to_element_with_wait(locator_formatted)

    @allure.step('Проверяем видимость окна с деталями ингридиента')
    def check_ingredient_details_is_visible(self):
        return self.check_visibility_of_element(self.locators.INGREDIENT_DETAILS)

    @allure.step('Закрываем детали ингридиента')
    def click_to_close_details(self):
        self.click_to_element_with_wait(self.locators.INGRIDIENT_DETAILS_CLOSE)

    @allure.step('Проверяем что окно с деталями ингридиента не отображается')
    def check_ingredient_details_is_invisible(self):
        return self.check_element_is_invisible(self.locators.INGREDIENT_DETAILS)

    def add_bun(self):
        test_data = GenerateTestData()
        bun = test_data.bun()
        locator_drag = self.format_locators(self.locators.INGREDIENT_LOCATOR, bun)
        self.drag_and_drop(locator_drag, self.locators.BUCKET)

    def add_sauce(self):
        test_data = GenerateTestData()
        sauce = test_data.sauce()
        locator_drag = self.format_locators(self.locators.INGREDIENT_LOCATOR, sauce)
        self.drag_and_drop(locator_drag, self.locators.BUCKET)

    def add_filling(self):
        test_data = GenerateTestData()
        filling = test_data.filling()
        locator_drag = self.format_locators(self.locators.INGREDIENT_LOCATOR, filling)
        self.drag_and_drop(locator_drag, self.locators.BUCKET)

    def get_bucket_counter_value(self):
        value = int(
            self.get_text_from_element(self.locators.BUCKET_COUNTER))
        return value

    @allure.step('Добавляем ингредиент и возвращаем значение счетчика ингридиента')
    def add_ingredient_return_ingr_counter(self, type):
        test_data = GenerateTestData()
        if type == "Bun":
            ingredient = test_data.bun()
        elif type == "Sauce":
            ingredient = test_data.sauce()
        elif type == "Filling":
            ingredient = test_data.filling()
        locator_drag = self.format_locators(self.locators.INGREDIENT_LOCATOR, ingredient)
        self.drag_and_drop(locator_drag, self.locators.BUCKET)
        counter = self.ingredient_counter(locator_drag)
        return counter

    def ingredient_counter(self, locator_raw):
        method, locator = locator_raw
        locator_ingr_counter = f'{locator}{data.TestData.ingredient_counter}'
        locator_ingr_counter = method, locator_ingr_counter
        counter = int(
            self.get_text_from_element(locator_ingr_counter))
        return counter

    @allure.step('Ожидаем пока 9999 изменится на номер заказа')
    def wait_default_num_invisibility(self):
        self.wait_for_element_invisibility(self.locators.DEFAULT_ORDER_NUMBER)

    @allure.step('Кликаем на кнопку оформить заказ')
    def click_to_order_button(self):
        self.click_to_element_with_wait(self.locators.ORDER_BUTTON)

    @allure.step('Кликаем на кнопку войти в аккаунт')
    def click_to_login_button(self):
        self.click_to_element_with_wait(self.locators.LOGIN_ACCOUNT_BUTTON)

    @allure.step('Проверяем видимость окна заказом')
    def check_order_window_is_visible(self):
        return self.check_visibility_of_element(self.locators.ORDER_COMPLETE_BOX)

    def get_order_number(self):
        order_number = str(self.get_text_from_element(self.locators.ORDER_NUMBER))
        return order_number

    def click_to_cross_button(self):
        self.click_to_element_with_wait(self.locators.CROSS_BUTTON)

    @allure.step('Делаем бургер и возвращаем номер заказа')
    def make_burger(self):
        self.click_to_constructor_button()
        self.add_bun()
        self.add_filling()
        self.add_sauce()
        self.click_to_order_button()
        self.wait_default_num_invisibility()
        order_number = self.get_order_number()
        self.click_to_cross_button()
        return order_number
