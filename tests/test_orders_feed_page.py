import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage


@allure.feature('Раздел «Лента заказов»')
class TestOrdersFeedPage:
    @allure.title('Открытие окна с деталями заказа')
    @allure.description('Проверка если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_details_window(self, driver):
        orders_feed = OrdersFeedPage(driver)
        orders_feed.open(orders_feed.url)
        orders_feed.click_to_the_last_order()

        assert orders_feed.check_order_detail_page_is_visible()

    @allure.title('Заказы пользователя')
    @allure.description('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_users_order_in_orders_feed(self, driver, new_user):
        main_page = MainPage(driver)
        main_page.open(main_page.url)
        main_page.click_to_personal_account_button()
        login_page = LoginPage(driver)
        login_page.user_login(new_user)
        order_number = main_page.make_burger()
        orders_feed = OrdersFeedPage(driver)
        orders_done = orders_feed.get_orders_done()

        assert order_number in orders_done, \
            f'Ошибка: номер заказа {order_number} отсутствует в списке заказов {orders_done}'

    @allure.title('Счетчик Выполнено за всё время')
    @allure.description('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_counter_all_orders_increase(self, driver, new_user):
        main_page = MainPage(driver)
        main_page.open(main_page.url)
        main_page.click_to_personal_account_button()
        login_page = LoginPage(driver)
        login_page.user_login(new_user)
        main_page.click_to_orders_feed_button()
        orders_feed = OrdersFeedPage(driver)
        all_orders = orders_feed.get_all_orders_count()
        main_page.make_burger()
        main_page.click_to_orders_feed_button()
        all_orders_after_order = orders_feed.get_all_orders_count()
        expected_result = all_orders + 1

        assert all_orders_after_order == expected_result, \
            f'Ошибка: не изменился общий счетчик заказов после заказа'

    @allure.title('Счетчик Выполнено за сегодня')
    @allure.description('Проверка, что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_counter_today_orders_increase(self, driver, new_user):
        main_page = MainPage(driver)
        main_page.open(main_page.url)
        main_page.click_to_personal_account_button()
        login_page = LoginPage(driver)
        login_page.user_login(new_user)
        main_page.click_to_orders_feed_button()
        orders_feed = OrdersFeedPage(driver)
        today_orders = orders_feed.get_today_orders_count()
        main_page.make_burger()
        main_page.click_to_orders_feed_button()
        today_orders_after_order = orders_feed.get_today_orders_count()
        expected_result = today_orders + 1

        assert today_orders_after_order == expected_result, \
            f'Ошибка: не изменился счетчик сегодняшних заказов после заказа'

    @allure.title('Заказ в работе')
    @allure.description('Проверка, что после оформления заказа его номер появляется в разделе В работе')
    def test_order_in_work_after_creation(self, driver, new_user):
        main_page = MainPage(driver)
        main_page.open(main_page.url)
        main_page.click_to_personal_account_button()
        login_page = LoginPage(driver)
        login_page.user_login(new_user)
        orders_feed = OrdersFeedPage(driver)
        order_number = main_page.make_burger()
        main_page.click_to_orders_feed_button()
        orders_in_work = orders_feed.get_orders_in_work()

        assert order_number in orders_in_work, \
            f'Ошибка: номер заказа {order_number} отсутствует в списке заказов {orders_in_work}'
