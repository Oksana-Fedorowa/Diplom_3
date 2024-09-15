import allure
from data import Data
from page_objects.main_page import MainPage
from page_objects.feed_page import FeedPage
from page_objects.password_recovery_page import PasswordRecoveryPage



class TestMainPage:

    @allure.title('Тест: Перход на страницу логина по клику на "Личный кабинет"')
    def test_click_login_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_for_modal_to_disappear()
        main_page.click_on_account_button()
        p_r_page = PasswordRecoveryPage(driver)
        assert p_r_page.find_login_button()


    @allure.title('Тест: Переход по клику "Конструктор"')
    def test_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Data.LOGIN_URL)
        main_page.find_burger_constructor_button()
        main_page.wait_for_modal_to_disappear()
        main_page.click_on_constructor_button()
        assert main_page.find_burger_constructor_title()

    @allure.title('Тест: Переход по клику "Лента заказов"')
    def test_orders_feed_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_for_modal_to_disappear()
        main_page.click_on_orders_feed_button()
        feed_page = FeedPage(driver)
        assert feed_page.find_feed_title()

    @allure.title('Тест: при клике на ингредиент, появится всплывающее окно с деталями,')
    def test_modal_after_clicking_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_for_modal_to_disappear()
        main_page.click_on_ingredient()
        assert main_page.find_ingredient_modal()

    @allure.title('Тест: Закрывается модальное окно ингредиента по клику на "крестик"')
    def test_modal_closure_by_clicking_x(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_for_modal_to_disappear()
        main_page.click_on_ingredient()
        main_page.close_ingredients_modal()
        assert main_page.find_is_ingredient_clickable()

    @allure.title('при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_add_ingredient_check_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        counter_0 = int(main_page.receive_ingredient_counter_text())
        main_page.drag_ingredient_to_basket()
        counter_1 = int(main_page.receive_ingredient_counter_text())
        assert counter_1 > counter_0

    @allure.title('Тест: Авторизованный пользователь может сделать заказ')
    def test_authorised_user_can_make_order(self, driver, registered_user):
        p_r_page = PasswordRecoveryPage(driver)
        main_page = MainPage(driver)
        main_page.wait_for_modal_to_disappear()
        p_r_page.login_into_account(registered_user)
        assert main_page.find_make_order_button()