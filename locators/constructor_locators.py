from selenium.webdriver.common.by import By

class ConstructorLocators:
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    INGREDIENT_BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    INGREDIENT_COUNTER = (By.XPATH,"//p[text()='Флюоресцентная булка R2-D3']/ancestor::a//p[contains(@class, 'counter_counter__num')]")
    INGREDIENT_DETAILS_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    INGREDIENT_DETAILS_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")
    BURGER_CONSTRUCTOR_BASKET = (By.XPATH,"//section[contains(@class,'BurgerConstructor_basket')]")
    LOADING_ANIMATION = (By.XPATH, "//img[@alt='loading animation']")
    ORDER_NUMBER_WINDOW = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")
    ORDER_WINDOW_CLOSE_BUTTON = (By.XPATH,"//div[contains(@class,'Modal_modal__')]//button")
    ORDER_NUMBER = (By.XPATH,"//div[contains(@class,'Modal_modal__')]//h2")