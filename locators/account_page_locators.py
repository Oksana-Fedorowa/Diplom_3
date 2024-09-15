from selenium.webdriver.common.by import By

class AccountPageLocators:
    BUTTON_ORDERS_HISTORY = By.XPATH, '//*[text()="История заказов"]' #история заказов лк
    ACTIVE_BUTTON_ORDER_HISTORY = By.XPATH, '//*[contains(@class, "Account_link_active") and text()="История заказов"]'#активная история заказов лк
    BUTTON_LOGOUT = By.XPATH, '//*[text()="Выход"]'#выход лк






