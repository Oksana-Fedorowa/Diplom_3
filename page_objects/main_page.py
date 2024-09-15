
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from data import Data
from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

class MainPage(BasePage):

    @allure.step("Ожидание, пока модальное окно не исчезнет")
    def wait_for_modal_to_disappear(self):
        try:
            WebDriverWait(self.driver, 20).until_not(
                expected_conditions.visibility_of_element_located(MainPageLocators.MODAL_OVERLAY)
            )
        except TimeoutException:
            raise TimeoutException("Модальное окно не исчезло в течение 20 секунд")

    @allure.step('Создаём заказ')
    def make_order(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT, MainPageLocators.PLACE_FOR_INGREDIENT)
        self.click_on_element(MainPageLocators.BUTTON_MAKE_ORDER)
        self.press_esc()

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.open_url(Data.BASE_URL)

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_on_account_button(self):
        self.click_on_element(MainPageLocators.BUTTON_ACCOUNT)






    @allure.step('Находим кнопку "конструктор"')
    def find_burger_constructor_button(self):
        element = self.find_element_with_wait(MainPageLocators.BUTTON_CONSTRUCTOR)
        return element.is_displayed()


    @allure.step('Клик по кнопке "Конструктор"')
    def click_on_constructor_button(self):
        self.click_on_element(MainPageLocators.BUTTON_CONSTRUCTOR)



    @allure.step('Находим заголовок "Соберите бургер"')
    def find_burger_constructor_title(self):
        element = self.find_element_with_wait(MainPageLocators.BURGER_CONSTRUCTOR_TITLE)
        return element.is_displayed()

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_on_orders_feed_button(self):
        self.click_on_element(MainPageLocators.BUTTON_ORDERS_FEED)


    @allure.step('Находим кнопку"Оформить заказ"')
    def find_make_order_button(self):
        element = self.find_element_with_wait(MainPageLocators.BUTTON_MAKE_ORDER)
        return element.is_displayed()

    @allure.step('Клик по ингредиенту')
    def click_on_ingredient(self):
        self.click_on_element(MainPageLocators.INGREDIENT)

    @allure.step('Проверяем кликабельность ингредиента')
    def find_is_ingredient_clickable(self):
        element = self.find_element_with_wait(MainPageLocators.INGREDIENT)
        return element.is_enabled()

    @allure.step('Находим модальное окно с описанием ингредиента')
    def find_ingredient_modal(self):
        element = self.find_element_with_wait(MainPageLocators.INGREDIENT_MODAL)
        return element.is_displayed()

    @allure.step('Клик по кнопке, закрывающей модальное окно с описанием ингредиента')
    def close_ingredients_modal(self):
        self.click_on_element(MainPageLocators.BUTTON_CLOSE_MODAL)

    @allure.step('Перетаскиваем булочку в заказ')
    def drag_ingredient_to_basket(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT, MainPageLocators.PLACE_FOR_INGREDIENT)

    @allure.step('Получаем информацию от счётчика ингредиента')
    def receive_ingredient_counter_text(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER)[0]

