import allure
import pytest

from data import TestData
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage


@allure.feature('Проверка основного функционала')
class TestMainPage:
    @allure.title('Переход по клику на «Конструктор»')
    @allure.description('Проверка перехода на страницу Конструктора на главной странице')
    def test_go_to_constructor_page(self, driver):
        main_page = MainPage(driver)
        main_page.open(main_page.url)
        main_page.click_to_constructor_button()

        assert main_page.check_constructor_page_is_visible()

    @allure.title('Переход по клику на «Лента заказов»')
    @allure.description('Проверка перехода на страницу ленты заказов')
    def test_go_to_orders_feed_page(self, driver):
        main_page = MainPage(driver)
        main_page.open(main_page.url)
        main_page.click_to_orders_feed_button()
        orders_feed_page = OrdersFeedPage(driver)

        assert orders_feed_page.check_orders_feed_page_is_visible()

    @allure.title('Появление окна с деталями при клике на ингридиент')
    @allure.description('Проверка если кликнуть на ингредиент, появится всплывающее окно с деталями. '
                        'Проверяется по 1 ингридиенту из разделов "Булки", "Соусы", "Начинки"')
    @pytest.mark.parametrize('ingredient', TestData.ingredients)
    def test_click_to_ingredient_pop_up_window(self, driver, ingredient):
        main_page = MainPage(driver)
        main_page.open(main_page.url)
        main_page.click_to_ingredient(ingredient)

        assert main_page.check_ingredient_details_is_visible()

    @allure.title('Закрытие всплывающего окна с деталями ингридиента')
    @allure.description('Проверка, что всплывающее окно закрывается кликом по крестику')
    @pytest.mark.parametrize('ingredient', TestData.ingredients)
    def test_close_pop_up_window_with_details(self, driver, ingredient):
        main_page = MainPage(driver)
        main_page.open(main_page.url)
        main_page.click_to_ingredient(ingredient)
        main_page.click_to_close_details()

        assert main_page.check_ingredient_details_is_invisible()

    @allure.title('Проверка, что при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    @allure.description('Проверяется для трех типов: булки, соусы, начинки')
    @pytest.mark.parametrize('ingredient_type, expected_counter', TestData.ingredient_type)
    def test_add_ingredient_to_order(self, driver, ingredient_type, expected_counter):
        main_page = MainPage(driver)
        main_page.open(main_page.url)
        counter = main_page.add_ingredient_return_ingr_counter(ingredient_type)

        assert counter == expected_counter

    @allure.title('Проверка, что залогиненный пользователь может оформить заказ')
    @allure.description('Создаем заказ с тремя ингридиентами, производим авторизацию и проверяем, что заказ оформился')
    def test_auth_user_can_create_order(self, driver, new_user):
        main_page = MainPage(driver)
        main_page.open(main_page.url)
        main_page.add_bun()
        main_page.add_sauce()
        main_page.add_filling()
        main_page.click_to_personal_account_button()
        login_page = LoginPage(driver)
        login_page.user_login(new_user)
        main_page.click_to_order_button()
        main_page.wait_default_num_invisibility()

        assert main_page.check_order_window_is_visible()


