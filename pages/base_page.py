import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищем элемент на странице {locator}')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Закрываем модальное окно по клику в углу, затем кликаем по элементу {locator}')
    def click_to_element_with_wait(self, locator):
        ActionChains(self.driver).move_by_offset(0, 0).click().perform()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Отправляем текст элементу {locator}')
    def send_text_to_the_element(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получаем текст элемента {locator}')
    def get_value_from_element(self, locator):
        return self.driver.find_element(*locator).get_attribute('value')

    @allure.step('Проверяем видимость элемента {locator}')
    def check_visibility_of_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.is_displayed()

    @allure.step('Открываем страницу {url}')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Ожидание видимости элемента {locator}')
    def wait_element_is_visible(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return element

    @allure.step('Получаем название класса для проверки активности поля')
    def get_class_name(self, locator):
        return self.wait_element_is_visible(locator).get_attribute('class')

    @allure.step('Форматируем локатор')
    def format_locators(self, locator_raw, ingredient):
        method, locator = locator_raw
        locator = locator.format(ingredient)
        return method, locator

    @allure.step('Ожидание видимости элемента {locator}')
    def check_element_is_invisible(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element(locator))
        return not element.is_displayed()

    @allure.step('Перетаскиваем элементы в заказ')
    def drag_and_drop(self, draggable_locator, droppable_locator):
        draggable_element = self.find_element_with_wait(draggable_locator)
        self.scroll_to_element(draggable_locator)
        droppable_element = self.find_element_with_wait(droppable_locator)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable_element, droppable_element).perform()

    def get_text_from_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        text = element.text
        return text

    @allure.step('Ждем скрытия элемента {locator}')
    def wait_for_element_invisibility(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))



