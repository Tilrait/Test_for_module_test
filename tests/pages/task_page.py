from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TaskPage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.ADD_TASK_LINK = (By.LINK_TEXT, "Добавить дело")
        self.TITLE = (By.ID, "title")
        self.ADD_BUTTON = (By.XPATH, '//input[@value="Добавить"]')
        self.SEARCH_INPUT = (By.NAME, "search")
        self.SEARCH_BUTTON = (By.XPATH, '//input[@value="Найти"]')

    def add_task(self, task_text):
        self.browser.find_element(*self.ADD_TASK_LINK).click()
        wait = WebDriverWait(self.browser, 10)
        input_field = wait.until(EC.element_to_be_clickable(self.TITLE))
        input_field.clear()
        input_field.send_keys(task_text)
        self.browser.find_element(*self.ADD_BUTTON).click()

    def search_task(self, task_text):
        search_field = self.browser.find_element(*self.SEARCH_INPUT)
        search_field.clear()
        search_field.send_keys(task_text)
        self.browser.find_element(*self.SEARCH_BUTTON).click()

    def mark_done(self, task_text):
        xpath = f'//a[. = "{task_text}"]/ancestor::article//input[@value="Сделано!"]'
        self.browser.find_element(By.XPATH, xpath).click()
        return self.browser.find_elements(By.XPATH, xpath)
