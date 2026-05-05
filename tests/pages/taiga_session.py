from selenium.webdriver.support.ui import WebDriverWait


class TaigaSession:
    @staticmethod
    def login_with_token(browser, base_url: str, token: str):
        """
        UI auth via existing Taiga auth token.

        Taiga front stores the auth token in localStorage under 'token'.
        """
        base_url = base_url.rstrip("/")

        browser.get(base_url)

        browser.execute_script("window.localStorage.setItem('token', arguments[0]);", token)

        browser.get(base_url)
        WebDriverWait(browser, 20).until(lambda d: d.execute_script("return window.localStorage.getItem('token');") == token)

