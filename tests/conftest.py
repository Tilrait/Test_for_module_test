import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome")
    parser.addoption("--language", action="store", default="ru")
    parser.addoption("--headless", action="store_true", default=False)

@pytest.fixture()
def browser(request):
    if request.config.getoption("browser") == "Firefox":
        browser = webdriver.Firefox()
    elif request.config.getoption("browser") == "Edge":
        browser = webdriver.Edge()
    else:
        options = Options()
        options.add_experimental_option(
            "prefs",
            {"intl.accept.languages": request.config.getoption("language")},
        )
        if request.config.getoption("--headless"):
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
        # Helps on macOS where Chrome isn't in PATH
        chrome_app = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        if os.path.exists(chrome_app):
            options.binary_location = chrome_app
        browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(3)
    yield browser
    browser.quit()