import allure
from pages.base_page import BasePage
from locators.base_locators import BaseLocators
from locators.constructor_locators import ConstructorLocators
from locators.order_feed_locators import OrderFeedLocators
from curl import *

class ConstructorPage(BasePage):

    @allure.step("Открываем страницу конструктора")
    def open_constructor_page(self):
        self.open(CONSTRUCTOR_URL)
        self.wait_for_page_fully_loaded()

    @allure.step("Перейти в раздел 'Конструктор'")
    def click_to_constructor_button(self):
        button = self.find(BaseLocators.CONSTRUCTOR_BUTTON)
        self.js_click(button)
        self.wait_for_page_fully_loaded()

    @allure.step("Перейти в раздел 'Лента заказов'")
    def click_to_order_feed_button(self):
        self.wait_until_element_not_visible(ConstructorLocators.LOADING_ANIMATION)
        self.wait_for_page_fully_loaded()
        button = self.wait_visibility_of_element(BaseLocators.ORDER_FEED_BUTTON)
        button.click()
        self.wait_visibility_of_element(OrderFeedLocators.ORDER_FEED_HEADER)

    @allure.step("Нажать на ингридиент")
    def click_ingredient(self):
        button = self.find(ConstructorLocators.INGREDIENT_BUN)
        self.js_click(button)
        self.wait_visibility_of_element(ConstructorLocators.INGREDIENT_DETAILS_TITLE)

    @allure.step("Проверяем появление всплывающего окна с доп. информацией об ингридиенте")    
    def is_details_window_visible(self):
        return self.is_element_visible(ConstructorLocators.INGREDIENT_DETAILS_TITLE)

    @allure.step("Закрываем окно через нажатие на крестик")
    def close_ingredient_window(self):
        button = self.find(ConstructorLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)
        self.js_click(button)
        self.wait_until_element_not_visible(ConstructorLocators.INGREDIENT_DETAILS_TITLE)

    @allure.step("Проверяем закрытие всплывающего окна с доп. информацией об ингридиенте")    
    def is_details_window_closed(self):
        return self.wait_until_element_not_visible(ConstructorLocators.INGREDIENT_DETAILS_TITLE)

    @allure.step("Добавляем ингредиент")
    def add_ingredients_to_order(self):
        self.drag_element(ConstructorLocators.INGREDIENT_BUN, ConstructorLocators.BURGER_CONSTRUCTOR_BASKET)

    @allure.step("Получаем количество добавленного ингредиента с счетчика")
    def get_quantity_of_ingredients(self):
        return int(self.get_text(ConstructorLocators.INGREDIENT_COUNTER))

    @allure.step("Нажимаем на кнопку 'Оформить заказ'")
    def click_to_order_button(self):
        button = self.find(ConstructorLocators.ORDER_BUTTON)
        self.js_click(button)
        self.wait_visibility_of_element(ConstructorLocators.ORDER_NUMBER_WINDOW)

    @allure.step("Получаем номер заказа")
    def get_order_number(self):
        number = self.wait_visibility_of_element(ConstructorLocators.ORDER_NUMBER)
        return number.text
    
    @allure.step("Закрываем окно заказа")
    def close_order_window(self):
        button = self.find(ConstructorLocators.ORDER_WINDOW_CLOSE_BUTTON)
        self.js_click(button)
        self.wait_until_element_not_visible(ConstructorLocators.ORDER_NUMBER_WINDOW)

    @allure.step("Ожидаем полной загрузки окна заказа")
    def wait_loading_order_window(self):
        self.wait_visibility_of_element(ConstructorLocators.LOADING_ANIMATION)
        self.wait_until_element_not_visible(ConstructorLocators.LOADING_ANIMATION)
        self.wait_visibility_of_element(ConstructorLocators.ORDER_NUMBER)
        self.wait_visibility_of_element(ConstructorLocators.ORDER_WINDOW_CLOSE_BUTTON)
