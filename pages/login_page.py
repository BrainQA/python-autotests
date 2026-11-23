from selenium.webdriver.common.by import By

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
        self.type(self.USERNAME_FIELD, username)

    # Вводим Password
    def enter_password(self, password):
        self.type(self.PASSWORD_FIELD, password)

    # Нажимаем Login
    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    # Получаем сообщение
    def get_flash_message(self):
        return self.get_text(self.FLASH_MESSAGE)

    # Выполняем авторизацию
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
