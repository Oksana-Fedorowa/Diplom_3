from selenium.webdriver.common.by import By


class FeedPageLocators:
    FEED_PAGE_TITLE = By.XPATH, '//*[text()="Лента заказов"]' #заголовок лента заказов

    BUTTON_CLOSE_MODAL = By.XPATH, '//*[contains(@class, "modal__close") and @type="button"]'#Кнопка закрывающая окно с деталями заказа

    MODAL_ORDER_NUMBER = By.XPATH, '//h2[contains(@class, "modal__title")]' #номер заказа до

    ORDER = By.XPATH, '//div[contains(@class, "OrderHistory")]//child::a'

    ORDER_MODAL = By.XPATH, '//section[contains(@class, "modal_opened")]'

    ORDER_NUMBER = By.XPATH, '//*[@class="text text_type_digits-default"]'#номер заказа в ленте

    ALL_TIME_COUNTER = By.XPATH, '//*[text()="Выполнено за все время:"]/following::p'#счетчик выполнено за все время

    TODAY_COUNTER = By.XPATH, '//*[text()="Выполнено за сегодня:"]/following::p'#счетчик выполнено за сегодня

    IN_PROGRESS_LIST = By.XPATH, '//*[contains(@class, "orderListReady")]/child::li[@class="text text_type_digits-default mb-2"]'#в работе

    MODAL_OVERLAY = By.XPATH, '//*[contains(@class,  "Modal_modal__loading")]/following::div[@class="Modal_modal_overlay__x2ZCr"]'  # модально окно мешающее