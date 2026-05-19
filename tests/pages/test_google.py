from tests.pages.login_page import LoginPage
from tests.pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://google.com"
    page = MainPage(browser, link)
    page.open()


def test_guest_can_see_login_page1231234(browser):
    link = "http://google.com"
    page = MainPage(browser, link)
    page.open()


def test_guest_can(browser):
    link = "http://google.com"
    page = MainPage(browser, link)
    page.open()


def test_guest_can2(browser):
    link = "http://google.com"
    page = MainPage(browser, link)
    page.open()


def test_guest_can3(browser):
    link = "http://firefox.com"
    page = MainPage(browser, link)
    page.open()
