
from page_objects.account_page import AccountPage
from page_objects.main_page import MainPage
from page_objects.password_recovery_page import PasswordRecoveryPage
import allure


class TestAccountPage:
    @allure.title('Тест: Перход на страницу логина по клику на "Личный кабинет"')
    def test_click_login_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_account_button()
        account_page = AccountPage(driver)
        assert account_page.find_login_button()

    @allure.title('Тест: Переход по клику на "История заказов"')
    def test_get_order_history_page_by_button(self, driver, registered_user):
        payload = registered_user
        account_page = AccountPage(driver)
        account_page.login_into_account(payload)
        main_page = MainPage(driver)
        main_page.click_on_account_button()
        account_page.click_on_orders_history_button()
        assert account_page.find_history_order_block()

    @allure.title('Проверка выполнения логаута по кнопке "Выйти"')
    def test_logout_by_logout_button(self, driver, registered_user):
        payload = registered_user
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        password_recovery_page = PasswordRecoveryPage(driver)
        account_page.login_into_account(payload)
        main_page.click_on_account_button()
        account_page.click_on_logout_button()
        assert password_recovery_page.find_enter_button()
