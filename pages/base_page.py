import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
from curl import *

class BasePage:

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открытие страниыцы по url")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Поиск элемента по локатору")
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    @allure.step("Клик по элементу")
    def click(self, locator):
        self.find(locator).click()

    @allure.step("Внесение данных в поле с определенным локатором")
    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста элемента")
    def get_text(self, locator):
        return self.find(locator).text
    
    @allure.step("Проверка видимости элемента на экране")    
    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
        
    @allure.step("Получение текущего url")        
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Клик на элемент через JavaScript")
    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ожидаем, пока элемент станет кликабельным, и возвращаем его")
    def wait_element_to_be_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидает видимости элемента и возвращает его")
    def wait_visibility_of_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step('Перемещение элемента')
    def drag_element(self, source, target):
        drag_and_drop(self.driver, self.driver.find_element(*source), self.driver.find_element(*target))

    @allure.step("Ожидание невидимости элемента")
    def wait_until_element_not_visible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))
    
    @allure.step("Дожидаемся полной загрузки страницы")
    def wait_for_page_fully_loaded(self):
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")