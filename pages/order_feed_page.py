import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from curl import *

class OrderFeedPage(BasePage):

    @allure.step("Ожидаем загрузки страницы 'Лента Заказов'")
    def wait_order_feed_is_opened(self):
        return self.wait_visibility_of_element(OrderFeedLocators.ORDER_FEED_HEADER).is_displayed()

    @allure.step("Открываем страницу Лента Заказов")
    def open_order_feed_page(self):
        self.open(ORDER_FEED_URL)
        self.wait_order_feed_is_opened()

    @allure.step("Получаем данные из счетчика 'Выполнено за все время'")
    def get_orders_all_time_counter(self):
        self.wait_order_feed_is_opened()
        self.wait_visibility_of_element(OrderFeedLocators.ALL_TIME_COUNTER)
        counter = self.get_text(OrderFeedLocators.ALL_TIME_COUNTER)
        return int(counter)

    @allure.step("Получаем данные из счетчика 'Выполнено за сегодня'")
    def get_orders_today_counter(self):
        self.wait_order_feed_is_opened()
        self.wait_visibility_of_element(OrderFeedLocators.TODAY_ORDERS_COUNTER)
        counter = self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNTER)
        return int(counter)
    
    @allure.step('Получение номера заказа из списка "В работе"')
    def get_order_in_progress(self):
        self.wait_order_feed_is_opened()
        order = self.wait_visibility_of_element(OrderFeedLocators.ORDER_IN_PROGRESS)
        return order.text
    