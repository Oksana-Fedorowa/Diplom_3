from selenium.webdriver.common.by import By

class MainPageLocators:

    BUTTON_ACCOUNT = By.XPATH, '//*[text()="Личный Кабинет"]'#Кнпка Личный кабинет

    #BUTTON_ACCOUNT = By.XPATH, "//a[@href='/account']"

    BUTTON_CONSTRUCTOR = By.XPATH, '//*[text()="Конструктор"]'#кнопка конструктор

    #BUTTON_ORDERS_FEED = By.XPATH, '//*[text()="Лента Заказов"]' #лента заказов
    BUTTON_ORDERS_FEED = (By.XPATH, "//a[@href='/feed']")

    BURGER_CONSTRUCTOR_TITLE = By.XPATH, '//*[text()="Соберите бургер"]'#заголовок соберите бургер

    INGREDIENT = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d" and @draggable]'#булочка

    INGREDIENT_MODAL = By.XPATH, '//*[contains(@class, "contentBox")]'#детали ингредиента

    BUTTON_CLOSE_MODAL = By.XPATH, '//*[contains(@class, "modal__close") and @type="button"]'#кнопка закрытия окна детали ингредиента

    INGREDIENT_COUNTER = By.XPATH, '//p[contains(@class, "counter")]' #счетчик кол-ва ингредиента

    PLACE_FOR_INGREDIENT = By.XPATH, '//section[contains(@class,"BurgerConstructor_basket")]'#блок куда перетаскивать ингредиенты

    BUTTON_MAKE_ORDER = By.XPATH, '//*[text()="Оформить заказ"]'#кнопка оформить заказ

    MODAL_OVERLAY = By.XPATH,'//*[contains(@class,  "Modal_modal__loading")]/following::div[@class="Modal_modal_overlay__x2ZCr"]'#модально окно мешающее





