import allure
import pytest
from selenium import webdriver
from curl import BASE_URL
from pages.login_page import LoginPage
from valid_data import *

@allure.description("Открытие и закрытие браузера")
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    with allure.step(f"Запуск браузера: {browser_name}"):
        if request.param == "chrome":
            driver = webdriver.Chrome()
        elif request.param == "firefox":
            driver = webdriver.Firefox()
    driver.maximize_window()
    with allure.step("Открытие главной страницы"):
        driver.get(BASE_URL)
    yield driver
    with allure.step("Закрытие браузера"):
        driver.delete_all_cookies()
        driver.quit()

@allure.description("Авторизация пользователя")
@pytest.fixture
def authorized_user(driver):
    login_page = LoginPage(driver)
    login_page.login(registration_email, registration_password)
