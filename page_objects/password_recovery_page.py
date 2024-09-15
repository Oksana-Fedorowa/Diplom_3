from page_objects.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators
import allure
from data import Data

class PasswordRecoveryPage(BasePage):

    @allure.step('Переходит на страницу логина')
    def open_login_page(self):
        self.open_url(Data.LOGIN_URL)

    @allure.step('Входим в аккаунт')
    def login_into_account(self, payload):
        self.open_url(Data.LOGIN_URL)
        self.text_input_to_element(PasswordRecoveryLocators.INPUT_EMAIL, payload["email"])
        self.text_input_to_element(PasswordRecoveryLocators.INPUT_PASSWORD, payload["password"])
        self.click_on_element(PasswordRecoveryLocators.BUTTON_LOGIN)


    @allure.step('Кликает по кнопке "Восстановить пароль"')
    def click_on_restore_pass_button(self):
        self.scroll_to_element(PasswordRecoveryLocators.BUTTON_RESTORE_PASS)
        self.click_on_element(PasswordRecoveryLocators.BUTTON_RESTORE_PASS)

    @allure.step('Вводит электронный адрес пользователя')
    def enter_mail(self, mail):
        self.text_input_to_element(PasswordRecoveryLocators.INPUT_EMAIL, mail)

    @allure.step('Находим кнопку "Войти"')
    def find_login_button(self):
        element = self.find_element_with_wait(PasswordRecoveryLocators.BUTTON_LOGIN)
        return element.is_displayed()



    @allure.step('Находит кнопку "Восстановить"')
    def find_restore_button(self):
        element = self.find_element_with_wait(PasswordRecoveryLocators.BUTTON_RESTORE)
        return element.is_displayed()

    @allure.step('Находит поле  ввода кода из письма')
    def find_code_from_mail_field(self):
        element = self.find_element_with_wait(PasswordRecoveryLocators.INPUT_CODE)
        return element.is_displayed()

    @allure.step('Кликает по кнопке "Восстановить"')
    def click_on_restore_button(self):
        self.click_on_element(PasswordRecoveryLocators.BUTTON_RESTORE)

    @allure.step('Клик иконки скрывающей пароль')
    def click_on_see_pass_button(self):
        self.click_on_element(PasswordRecoveryLocators.BUTTON_SEE_PASS)

    @allure.step('Проверяет, что поле ввода пароля активно')
    def find_is_password_input_active(self):
        element = self.find_element_with_wait(PasswordRecoveryLocators.ACTIVE_INPUT_PASSWORD)
        return element.is_displayed()







