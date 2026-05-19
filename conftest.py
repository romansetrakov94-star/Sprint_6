import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config import Config

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="Browser: chrome or firefox")

@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("browser.privatebrowsing.autostart", False)
        options.set_preference("browser.aboutwelcome.enabled", False)
        driver = webdriver.Firefox(options=options)
    else:
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        options = ChromeOptions()
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    driver.get(Config.BASE_URL)

    # Закрываем баннер с куками, если есть
    try:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        cookie_btn = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        cookie_btn.click()
    except:
        pass

    yield driver
    driver.quit()
    