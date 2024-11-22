from selenium.webdriver.common.by import By


class OrdersFeedPageLocators:
    ORDERS_FEED_PAGE = By.XPATH, ".//h1[text()='Лента заказов']"
    LAST_ORDER = By.XPATH, ".//div[contains(@class,'OrderHistory_dataBox__1mkxK')]"
    ORDER_DETAIL_BOX = By.XPATH, "//div[contains(@class,'Modal_orderBox__1xWdi')]"
    ALL_ORDERS = By.XPATH, "//div[2]/p[contains(@class,'OrderFeed_number__2MbrQ')]"
    TODAY_ORDERS = By.XPATH, "//div[3]/p[contains(@class,'OrderFeed_number__2MbrQ')]"
    ORDERS_IN_WORK = By.XPATH, "//ul[2]/li[contains(@class,'text text_type_digits-default')]"
    ORDERS_DONE = By.XPATH, "//ul[1][contains(@class,'OrderFeed_orderList')]"
    ORDER_COMPOUND = By.XPATH, "//div/p[3][text()='Cостав']"
