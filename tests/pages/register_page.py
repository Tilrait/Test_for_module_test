from .base_page import BasePage
from .locators import RegisterPageLocators


class RegisterPage(BasePage):
    def open(self):
        self.browser.get(self.url + "/register")

    def register(self, username, password):
        self.click(*RegisterPageLocators.REGISTER_LINK)
        self.type(*RegisterPageLocators.USERNAME, username)
        self.type(*RegisterPageLocators.PASSWORD, password)
        self.type(*RegisterPageLocators.PASSWORD2, password)
        self.click(*RegisterPageLocators.SUBMIT)

    def is_logged_in(self):
        return len(self.finds(*RegisterPageLocators.LOGOUT_BTN)) > 0

    def delete_account(self, password):
        self.click(*RegisterPageLocators.DELETE_BTN)
        self.type(*RegisterPageLocators.DELETE_CONFIRM, password)
        self.click(*RegisterPageLocators.DELETE_SUBMIT)
