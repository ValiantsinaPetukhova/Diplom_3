import allure

from pages.base_page import BasePage
import data


class HistoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = data.Urls.ORDERS_HISTORY_URL

    @allure.step('Получаем страничку истории заказов пользователя')
    def check_history_url(self):
        curr_url = self.get_current_url()
        return curr_url == self.url