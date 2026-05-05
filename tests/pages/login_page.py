from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.USERNAME_FIELD = (By.NAME, "username")
        self.PASSWORD_FIELD = (By.NAME, "password")
        self.LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')
        self.OPEN_LOGIN_FORM = (By.CLASS_NAME, "button")
        self.ERRORS = (By.CSS_SELECTOR, ".label.error")

    def open(self):
        self.browser.get(self.url)
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(self.OPEN_LOGIN_FORM)
        ).click()

    def login(self, username, password):
        wait = WebDriverWait(self.browser, 10)

        username_field = wait.until(EC.presence_of_element_located(self.USERNAME_FIELD))
        username_field.clear()
        username_field.send_keys(username)

        password_field = self.browser.find_element(*self.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)

        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def get_errors(self):
        return self.browser.find_elements(*self.ERRORS)
