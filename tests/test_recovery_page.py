import allure

from data import TestData
from pages.login_page import LoginPage
from pages.recovery_page import RecoveryPage


@allure.feature('Восстановление пароля')
class TestRecoveryPage:
    @allure.title('Проверка перехода на страницу восстановления пароля по ссылке «Восстановить пароль»')
    @allure.description('На странице авторизации нажимаем ссылку «Восстановить пароль» и проверяем, '
                        'что отображается страница воостановления пароля')
    def test_go_to_recovery_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open(login_page.url)
        login_page.click_to_recovery_link()
        recovery_page = RecoveryPage(driver)

        assert recovery_page.check_recovery_page_is_visible()

    @allure.title('Проверка ввода почты на странице восстановления')
    @allure.description('Открываем страницу восстановления, вводим значение почты и проверяем, '
                        'что это значение соответствует ожидаемому')
    def test_fill_in_email_for_recovery(self, driver, new_user):
        recovery_page = RecoveryPage(driver)
        recovery_page.open(recovery_page.url)
        recovery_page.fill_in_email_field(new_user)
        result = recovery_page.get_email()
        expected_result = new_user["email"]

        assert result == expected_result

    @allure.title('Проверка, что после ввода почты и нажатия на кнопку "Восстановить" происходит '
                        'переход на страницу для ввода пароля')
    @allure.description('Открываем страницу восстановления, вводим значение почты и нажимаем на кнопку "Восстановить".'
                        'Проверяем, что отображается страница для ввода нового пароля')
    def test_click_to_recovery_button(self, driver, new_user):
        recovery_page = RecoveryPage(driver)
        recovery_page.open(recovery_page.url)
        recovery_page.fill_in_email_field(new_user)
        recovery_page.click_to_recovery_button()

        assert recovery_page.check_recovery_page_is_visible()

    @allure.title('Проверка, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.description('Открываем страницу восстановления, вводим значение почты и нажимаем на кнопку "Восстановить".'
                        'На странице для ввода нового пароля нажимаем на значок "глаз" и проверяем, '
                        'что изменилось имя класса элемента')
    def test_click_to_eye_button_in_password_field(self, driver, new_user):
        recovery_page = RecoveryPage(driver)
        recovery_page.open(recovery_page.url)
        recovery_page.fill_in_email_field(new_user)
        recovery_page.click_to_recovery_button()
        recovery_page.wait_recovery_page()
        recovery_page.click_to_eye_button()
        class_name = recovery_page.get_eye_class_name()

        assert TestData.password_class_name in class_name, \
            f'Ошибка: не подсветилось поле "Пароль" после нажатия на глаз'