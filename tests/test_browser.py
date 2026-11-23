from selenium import webdriver


def test_open_browser(driver):
    # driver = webdriver.Chrome()
    driver.get("https://google.com")  # noqa: F821
    assert driver.title == "Google"
    driver.quit()
