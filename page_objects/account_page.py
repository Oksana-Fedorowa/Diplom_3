from page_objects.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
import allure



class AccountPage(BasePage):

    @allure.step('Клик по кнопке "История заказов"')
    def click_on_orders_history_button(self):
        self.click_on_element(AccountPageLocators.BUTTON_ORDERS_HISTORY)

    @allure.step('Находим блок с историей заказов')
    def find_history_order_block(self):
        element = self.find_element_with_wait(AccountPageLocators.ACTIVE_BUTTON_ORDER_HISTORY)
        return element.is_displayed()

    @allure.step('Клик по кнопке "Выход"')
    def click_on_logout_button(self):
        self.click_on_element(AccountPageLocators.BUTTON_LOGOUT)
















