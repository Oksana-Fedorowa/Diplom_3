from page_objects.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from locators.password_recovery_locators import PasswordRecoveryLocators
from selenium.common import ElementClickInterceptedException
from locators.main_page_locators import MainPageLocators
import allure
from data import Data

class AccountPage(BasePage):
    @allure.step('Входим в аккаунт')
    def login_into_account(self, payload):
        self.open_url(Data.LOGIN_URL)
        self.wait_for_modal_to_disappear(MainPageLocators.MODAL_OVERLAY)
        self.text_input_to_element(PasswordRecoveryLocators.INPUT_EMAIL, payload["email"])
        self.text_input_to_element(PasswordRecoveryLocators.INPUT_PASSWORD, payload["password"])
        self.click_on_element(PasswordRecoveryLocators.BUTTON_LOGIN)

    @allure.step('Клик по кнопке "История заказов"')
    def click_on_orders_history_button(self):
        self.wait_for_modal_to_disappear(MainPageLocators.MODAL_OVERLAY)
        self.click_on_element(AccountPageLocators.BUTTON_ORDERS_HISTORY)



    @allure.step('Находим блок с историей заказов')
    def find_history_order_block(self):
        element = self.find_element_with_wait(AccountPageLocators.ACTIVE_BUTTON_ORDER_HISTORY)
        return element.is_displayed()

    @allure.step('Клик по кнопке "Выход"')
    def click_on_logout_button(self):
        self.wait_for_modal_to_disappear(MainPageLocators.MODAL_OVERLAY)
        self.click_on_element(AccountPageLocators.BUTTON_LOGOUT)



    @allure.step('Находим кнопку "Войти"')
    def find_login_button(self):
        element = self.find_element_with_wait(PasswordRecoveryLocators.BUTTON_LOGIN)
        return element.is_displayed()

