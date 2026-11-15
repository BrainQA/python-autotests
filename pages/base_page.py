from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Поиск видимого элемента
    def find_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    # Нажатие кнопки
    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    # Ввод текста
    def type(self, locator, text):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    # Получение текста элемента
    def get_text(self, locator):
        return self.find_visible(locator).text

    # Открытие страницы
    def open_url(self, url):
        self.driver.get(url)
