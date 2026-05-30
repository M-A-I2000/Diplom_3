import allure
from curl import *
from pages.order_feed_page import OrderFeedPage
from pages.constructor_page import ConstructorPage

class TestMainPage:

    @allure.title("Проверяем переход в раздел конструктор по кнопке «Конструктор»")
    @allure.description("Открываем страницу с лентой заказов и нажимаем на кнопку 'Конструктор'.")
    def test_navigate_to_constructor_via_click(self, driver):
        order_feed_page = OrderFeedPage(driver)
        constructor_page = ConstructorPage(driver)
        order_feed_page.open_order_feed_page()
        constructor_page.click_to_constructor_button()

        assert constructor_page.get_current_url() == CONSTRUCTOR_URL

    @allure.title("Проверяем переход в раздел «Лента заказов»")
    @allure.description("Открываем начальную страницу и нажимаем на кнопку «Лента заказов».")
    def test_navigate_to_order_feed_via_click(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_to_order_feed_button()

        assert constructor_page.get_current_url() == ORDER_FEED_URL


    @allure.title("Проверка появления всплывающего окна с деталями ингредиента при клике по элементу")
    @allure.description("Открываем начальную страницу, переходим в 'Конструктор' и нажимаем на ингридиент. Ожидааем, что всплывающее окно появилось.")
    def test_ingredient_click_opens_details_popup(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_ingredient()

        assert constructor_page.is_details_window_visible()


    @allure.title("Проверка закрытия всплывающего окна с деталями ингредиента по клику на крестик")
    @allure.description("Открываем начальную страницу, переходим в личный кабинет и нажимаем на кнопку 'Конструктор'.")
    def test_close_ingredient_popup_via_close_button(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_ingredient()
        constructor_page.close_ingredient_window()

        assert constructor_page.is_details_window_closed()


    @allure.title("Проверка добавления ингредиента в конструктор")
    @allure.description("Открываем начальную страницу, переходим в личный кабинет и нажимаем на кнопку 'Конструктор'.")
    def test_add_ingredient_to_constructor_is_success(self, driver):
        constructor_page = ConstructorPage(driver)
        counter = constructor_page.get_quantity_of_ingredients()
        constructor_page.add_ingredients_to_order()
        counter_after_adding = constructor_page.get_quantity_of_ingredients()

        assert counter_after_adding > counter