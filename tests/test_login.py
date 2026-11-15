import pytest

from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username, password, expected_message",
    [
        ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
        ("wronguser", "SuperSecretPassword!", "Your username is invalid!"),
        ("tomsmith", "wrongpass", "Your password is invalid!"),
        ("", "", "Your username is invalid!"),
    ],
    ids=[
        "successful_login",
        "invalid_username",
        "invalid_password",
        "empty_credentials",
    ],
)
def test_login_with_different_credentials(driver, username, password, expected_message):
    login_page = LoginPage(driver)

    # Открываем страницу
    login_page.open()

    # Выполняем авторизацию с переданными данными
    login_page.login(username, password)

    # Получаем сообщение
    message = login_page.get_flash_message()

    # Проверяем ожидаемый результат
    assert expected_message in message
