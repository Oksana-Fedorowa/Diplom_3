
from page_objects.account_page import AccountPage
from page_objects.main_page import MainPage
from page_objects.password_recovery_page import PasswordRecoveryPage
import allure


class TestAccountPage:

    @allure.title('Тест: Переход по клику на "История заказов"')
    def test_get_order_history_page_by_button(self, driver, registered_user):
        payload = registered_user
        p_r_page = PasswordRecoveryPage(driver)
        p_r_page.login_into_account(payload)
        main_page = MainPage(driver)
        main_page.click_on_account_button()
        account_page = AccountPage(driver)
        account_page.click_on_orders_history_button()
        assert account_page.find_history_order_block()

    @allure.title('Проверка выполнения логаута по кнопке "Выйти"')
    def test_logout_by_logout_button(self, driver, registered_user):
        payload = registered_user
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        p_r_page = PasswordRecoveryPage(driver)
        p_r_page.login_into_account(payload)
        main_page.click_on_account_button()
        account_page.click_on_logout_button()
        assert p_r_page.find_login_button()
