import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome")
    parser.addoption("--language", action="store", default="ru")
    parser.addoption("--headless", action="store_true", default=False)


@pytest.fixture()
def browser(request):
    if request.config.getoption("browser") == "Firefox":
        options = FirefoxOptions()
    elif request.config.getoption("browser") == "Edge":
        options = EdgeOptions()
    else:
        options = ChromeOptions()
        options.add_experimental_option(
            "prefs",
            {"intl.accept.languages": request.config.getoption("language")},
        )
        if request.config.getoption("--headless"):
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
        browser = webdriver.Remote(
            command_executor="http://localhost:4444", options=options
        )
    yield browser
    browser.quit()
