from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TaigaProjectPage:
    """
    Minimal UI helpers for Taiga project pages.

    Works with both Taiga Cloud and self-hosted instances as long as URLs follow:
    - /project/<project_slug>
    """

    def __init__(self, browser, base_url: str, project_slug: str):
        self.browser = browser
        self.base_url = base_url.rstrip("/")
        self.project_slug = project_slug.strip("/")

        self.KANBAN_LINK = (By.CSS_SELECTOR, 'a[href*="/kanban"], [data-test="project-kanban"]')
        self.BACKLOG_LINK = (By.CSS_SELECTOR, 'a[href*="/backlog"], [data-test="project-backlog"]')

        # "Create US" controls vary between versions; keep multiple fallbacks.
        self.NEW_US_BUTTON = (
            By.CSS_SELECTOR,
            '[data-test="new-user-story"], button[title*="User Story"], button[title*="user story"], '
            'a[title*="User Story"], a[title*="user story"], .create-us, .new-us, .btn-create',
        )
        self.NEW_US_SUBJECT = (By.CSS_SELECTOR, 'input[name="subject"], input[placeholder*="Subject"], input[type="text"]')
        self.NEW_US_SAVE = (By.CSS_SELECTOR, 'button[type="submit"], button.save, .button.success')

        self.ITEM_TITLES = (By.CSS_SELECTOR, ".us-name, .card-title, .list-item-title, a[title]")

    def open(self):
        self.browser.get(f"{self.base_url}/project/{self.project_slug}")

    def open_backlog(self):
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.element_to_be_clickable(self.BACKLOG_LINK)).click()

    def create_user_story(self, title: str):
        wait = WebDriverWait(self.browser, 20)
        wait.until(EC.element_to_be_clickable(self.NEW_US_BUTTON)).click()

        subject = wait.until(EC.presence_of_element_located(self.NEW_US_SUBJECT))
        subject.clear()
        subject.send_keys(title)

        wait.until(EC.element_to_be_clickable(self.NEW_US_SAVE)).click()

    def has_title(self, title: str) -> bool:
        titles = self.browser.find_elements(*self.ITEM_TITLES)
        for el in titles:
            txt = (el.text or "").strip()
            if txt == title:
                return True
        return False

