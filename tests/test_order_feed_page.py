import allure
from pages.order_feed_page import OrderFeedPage
from pages.constructor_page import ConstructorPage
from valid_data import *

class TestOrderFeedPage:

    @allure.title('Проверка увеличения счётчика "Выполнено за всё время" при создании нового заказа') 
    @allure.description('Проверка текущего значения счетчика "Выполнено за всё время", создание заказа, авторизация, оформление заказа, проверка увеличения счетчика')
    def test_orders_all_time_counter_increases_after_order(self, driver, authorized_user):
        constructor_page = ConstructorPage(driver)
        order_feed_page = OrderFeedPage(driver)
        constructor_page.click_to_order_feed_button()
        init_counter = order_feed_page.get_orders_all_time_counter()
        constructor_page.click_to_constructor_button()
        constructor_page.add_ingredients_to_order()
        constructor_page.click_to_order_button()
        constructor_page.close_order_window()
        constructor_page.click_to_order_feed_button()
        
        assert order_feed_page.get_orders_all_time_counter() > init_counter

    @allure.title('Проверка увеличения счётчика "Выполнено за сегодня" при создании нового заказа') 
    @allure.description('Проверка текущего значения счетчика "Выполнено за сегодня", создание заказа, авторизация, оформление заказа, проверка увеличения счетчика')
    def test_orders_today_counter_increases_after_order(self, driver, authorized_user):
        constructor_page = ConstructorPage(driver)
        order_feed_page = OrderFeedPage(driver)
        constructor_page.click_to_order_feed_button()
        init_counter = order_feed_page.get_orders_today_counter()
        constructor_page.click_to_constructor_button()
        constructor_page.add_ingredients_to_order()
        constructor_page.click_to_order_button()
        constructor_page.close_order_window()
        constructor_page.click_to_order_feed_button()
        
        assert order_feed_page.get_orders_today_counter() > init_counter

    @allure.title("Проверка появления заказа в разделе 'В работе' после оформления заказа")
    @allure.description('Создаем закзаз за зарегистрированного пользователя и проверяем, что заказ попадает в раздел в работе')
    def test_order_number_appears_in_progress_list(self, driver, authorized_user):
        constructor_page = ConstructorPage(driver)
        order_feed_page = OrderFeedPage(driver)

        constructor_page.click_to_constructor_button()
        constructor_page.add_ingredients_to_order()
        constructor_page.click_to_order_button()
        constructor_page.wait_loading_order_window()
        order_number = constructor_page.get_order_number()
        constructor_page.close_order_window()
        
        constructor_page.click_to_order_feed_button()
        order_in_progress = order_feed_page.get_order_in_progress()
        
        assert order_number in order_in_progress
