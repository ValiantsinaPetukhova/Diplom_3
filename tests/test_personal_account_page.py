import allure

from pages.history_page import HistoryPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage


@allure.feature('Личный кабинет')
class TestPersonalAccountPage:
    @allure.title('Переход по клику на «Личный кабинет»')
    @allure.description('Проверка перехода на страницу личного кабинета')
    def test_go_to_personal_account_page(self, driver, new_user):
        login_page = LoginPage(driver)
        login_page.open(login_page.url)
        login_page.user_login(new_user)
        main_page = MainPage(driver)
        main_page.click_to_personal_account_button()
        profile_page = PersonalAccountPage(driver)

        assert profile_page.check_personal_account_is_visible()

    @allure.title('Переход по клику на страницу «История заказов»')
    @allure.description('Проверка перехода на страницу "История заказов" из личного кабинета')
    def test_go_to_orders_history_page(self, driver, new_user):
        login_page = LoginPage(driver)
        login_page.open(login_page.url)
        login_page.user_login(new_user)
        main_page = MainPage(driver)
        main_page.click_to_personal_account_button()
        profile_page = PersonalAccountPage(driver)
        profile_page.click_to_orders_history_button()
        history_page = HistoryPage(driver)

        assert history_page.check_history_url()

    @allure.title('Выход из аккаунта')
    @allure.description('Проверка выхода из аккаунта по кнопке из личного кабинета')
    def test_personal_account_logout(self, driver, new_user):
        login_page = LoginPage(driver)
        login_page.open(login_page.url)
        login_page.user_login(new_user)
        main_page = MainPage(driver)
        main_page.click_to_personal_account_button()
        profile_page = PersonalAccountPage(driver)
        profile_page.click_to_logout_button()

        assert login_page.check_login_page_is_visible()


