import allure
from data import Data
from page_objects.password_recovery_page import PasswordRecoveryPage
from page_objects.main_page import MainPage
from helpers import create_random_email
class TestPasswordRecoveryPage:
    @allure.title('Тест: Переход на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_get_forgot_password_page_by_button(self, driver):
        p_r_page = PasswordRecoveryPage(driver)
        p_r_page.open_login_page()
        main_page = MainPage(driver)
        main_page.wait_for_modal_to_disappear()
        p_r_page.click_on_restore_pass_button()
        assert p_r_page.find_restore_button()

    @allure.title('Тест: Ввод почты и клик "Восстановить"')
    def test_enter_mail_and_click_restore(self, driver):
        email = create_random_email()
        p_r_page = PasswordRecoveryPage(driver)
        p_r_page.open_url(Data.FORGOT_URL)
        p_r_page.enter_mail(email)
        main_page = MainPage(driver)
        main_page.wait_for_modal_to_disappear()
        p_r_page.click_on_restore_button()
        assert p_r_page.find_code_from_mail_field()

    @allure.title('Тест: Клик по кнопке показать/скрыть пароль делает поле активным— подсвечивает его.')
    def test_make_pass_field_visible(self, driver):
        p_r_page = PasswordRecoveryPage(driver)
        p_r_page.open_login_page()
        main_page = MainPage(driver)
        main_page.wait_for_modal_to_disappear()
        p_r_page.click_on_see_pass_button()
        assert p_r_page.find_is_password_input_active()
