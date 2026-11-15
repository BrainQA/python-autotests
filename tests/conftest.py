import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():

    # Открываем браузер
    driver = webdriver.Chrome()

    # Передаем браузер тесту
    yield driver

    # Закрываем браузер после теста
    driver.quit()