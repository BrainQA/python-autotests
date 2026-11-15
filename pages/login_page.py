from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.radius")
    FLASH_MESSAGE = (By.ID, "flash")

    URL = "https://the-internet.herokuapp.com/login"

    # Открываем страницу авторизации
    def open(self):
        self.open_url(self.URL)

    # Вводим Username
    def enter_username(self, username):
        username_field = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_FIELD)
        )
        username_field.send_keys(username)

    # Вводим Password
    def enter_password(self, password):
        password_field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_FIELD)
        )
        password_field.send_keys(password)

    # Нажимаем Login
    def click_login(self):
        login_button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()

    # Получаем сообщение
    def get_flash_message(self):
        message = self.wait.until(EC.visibility_of_element_located(self.FLASH_MESSAGE))
        return message.text

    # Выполняем авторизацию
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
