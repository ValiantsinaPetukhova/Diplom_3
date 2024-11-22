import allure

import data
from locators.orders_feed_locators import OrdersFeedPageLocators
from pages.base_page import BasePage


class OrdersFeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = data.Urls.FEED_URL
        self.locators = OrdersFeedPageLocators()

    @allure.step('Проверяем видимость страницы Лента заказов')
    def check_orders_feed_page_is_visible(self):
        return self.check_visibility_of_element(self.locators.ORDERS_FEED_PAGE)

    @allure.step('Кликаем на последний заказ')
    def click_to_the_last_order(self):
        self.click_to_element_with_wait(self.locators.LAST_ORDER)

    @allure.step('Проверяем видимость окна с деталями заказа')
    def check_order_detail_page_is_visible(self):
        return self.check_visibility_of_element(self.locators.ORDER_DETAIL_BOX)

    def open_orders_feed_page(self):
        self.open(self.url)

    @allure.step('Получаем количество всех заказов')
    def get_all_orders_count(self):
        self.open_orders_feed_page()
        all_orders = int(self.get_text_from_element(self.locators.ALL_ORDERS))
        return all_orders

    @allure.step('Получаем количество сегодняшних заказов')
    def get_today_orders_count(self):
        self.open_orders_feed_page()
        today_orders = int(self.get_text_from_element(self.locators.TODAY_ORDERS))
        return today_orders

    @allure.step('Получаем заказы в работе')
    def get_orders_in_work(self):
        self.open_orders_feed_page()
        orders_in_work = str(self.get_text_from_element(self.locators.ORDERS_IN_WORK))
        return orders_in_work

    @allure.step('Получаем готовые заказы')
    def get_orders_done(self):
        self.open_orders_feed_page()
        orders_done = str(self.get_text_from_element(self.locators.ORDERS_DONE))
        return orders_done