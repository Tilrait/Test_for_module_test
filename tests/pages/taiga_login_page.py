from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TaigaLoginPage:
    def __init__(self, browser, base_url: str):
        self.browser = browser
        self.base_url = base_url.rstrip("/")

        self.USERNAME = (By.CSS_SELECTOR, 'input[name="username"], input[name="email"], input[type="email"]')
        self.PASSWORD = (By.CSS_SELECTOR, 'input[name="password"], input[type="password"]')
        self.SUBMIT = (By.CSS_SELECTOR, 'button[type="submit"], input[type="submit"]')
        self.LOGIN_ERROR = (By.CSS_SELECTOR, ".errors, .error, .notification-error, .alert-error")

        # Post-login signals (Taiga variants)
        self.USER_MENU = (By.CSS_SELECTOR, ".user-avatar, .avatar, [data-test='user-menu'], .nav-user")

    def open(self):
        self.browser.get(f"{self.base_url}/login")

    def login(self, username: str, password: str):
        wait = WebDriverWait(self.browser, 15)
        username_el = wait.until(EC.presence_of_element_located(self.USERNAME))
        username_el.clear()
        username_el.send_keys(username)

        password_el = wait.until(EC.presence_of_element_located(self.PASSWORD))
        password_el.clear()
        password_el.send_keys(password)

        wait.until(EC.element_to_be_clickable(self.SUBMIT)).click()

    def wait_logged_in(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.USER_MENU))

    def get_login_errors(self):
        return self.browser.find_elements(*self.LOGIN_ERROR)

