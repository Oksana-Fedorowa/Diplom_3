
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains, Keys
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открывает указанный URL')
    def open_url(self, link):
        self.driver.get(link)

    @allure.step('Ищет элемент на странице , пока элемент не станет видимым')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)




    def click_on_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()


    @allure.step('Ввод значение в поле ввода')
    def text_input_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('возвращает текст, содержащийся в указанном элементе')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('прокручивает страницу до указанного элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('перетаскивает элемент с одного места на другое')
    def drag_and_drop_element(self, element_locator, destination_locator):
        from_element = self.find_element_with_wait(element_locator)
        to_element = self.find_element_with_wait(destination_locator)
        self.driver.execute_script("""
                const [from_element, to_element] = arguments;
                const dataTransfer = new DataTransfer();

                // Эмуляция событий drag-and-drop
                ['dragstart', 'dragover', 'drop', 'dragend'].forEach(eventType => {
                    const event = new DragEvent(eventType, { bubbles: true, cancelable: true, dataTransfer });
                    (eventType === 'dragstart' ? from_element : to_element).dispatchEvent(event);
                });
            """, from_element, to_element)

    @allure.step('Закрывает всплывающее окно')
    def press_esc(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()


