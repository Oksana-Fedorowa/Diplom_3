from selenium.webdriver.common.by import By

class AccountPageLocators:
    BUTTON_ORDERS_HISTORY = By.XPATH, '//*[text()="История заказов"]' #история заказов лк
    ACTIVE_BUTTON_ORDER_HISTORY = By.XPATH, '//*[contains(@class, "Account_link_active") and text()="История заказов"]'#активная история заказов лк
    BUTTON_LOGOUT = By.XPATH, '//*[text()="Выход"]'#выход лк
    MODAL_OVERLAY = By.XPATH, '//*[contains(@class,  "Modal_modal__loading")]/following::div[@class="Modal_modal_overlay__x2ZCr"]'  # модально окно мешающее





