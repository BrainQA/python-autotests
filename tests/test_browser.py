from selenium import webdriver

def test_open_browser():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    assert driver.title == "Google"
    driver.quit()