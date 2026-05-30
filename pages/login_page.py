import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from curl import *

class LoginPage(BasePage):
    
        
    @allure.step("Заполняем поле Email")        
    def enter_email(self, email):
        self.type(LoginLocators.EMAIL_INPUT, email)

    @allure.step("Заполняем поле пароль")
    def enter_password(self, password):
        self.type(LoginLocators.PASSWORD_INPUT, password)

    @allure.step("Нажимаем на кнопку 'Войти'")
    def click_login_button(self):
        self.wait_element_to_be_clickable(LoginLocators.LOGIN_BUTTON)
        button = self.find(LoginLocators.LOGIN_BUTTON)
        self.js_click(button)

    @allure.step("Заполняем форму авторизации")
    def fill_authorization_form(self, email, password):  
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    @allure.step("Залогиниваемся существующим пользователем")
    def login(self, email, password):
        self.open(LOGIN_URL)
        self.wait_for_page_fully_loaded()
        self.fill_authorization_form(email, password)
        self.wait_for_page_fully_loaded()