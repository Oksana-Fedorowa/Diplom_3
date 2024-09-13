from selenium.webdriver.common.by import By

class PasswordRecoveryLocators:
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following::input' # Поле ввода email

    INPUT_PASSWORD = By.XPATH, '//label[text()="Пароль"]/following::input'  # Поле ввода пароля

    BUTTON_RESTORE_PASS = By.XPATH, '//*[text()="Восстановить пароль"]' # Кнопка "Восстановить пароль" на экране входа

    INPUT_CODE = By.XPATH, '//*[text()="Введите код из письма"]' #поле ввода кода

    BUTTON_RESTORE = By.XPATH, '//*[text()="Восстановить"]' # Кнопка "Восстановить" на странице ввода email

    BUTTON_SEE_PASS = By.XPATH, '//*[@class="input__icon input__icon-action"]' # Иконка, скрывающая  пароль

    ACTIVE_INPUT_PASSWORD = By.XPATH, '//*[contains (@class, "placeholder-focused") and text()="Пароль"]' #поле пароля в восстановление

    BUTTON_LOGIN = By.XPATH, '//*[text()="Войти"]'  # кнопка войти



