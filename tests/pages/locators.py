from selenium.webdriver.common.by import By


class LoginPageLocators:
    BUTTON = (By.CLASS_NAME, "button")
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.CSS_SELECTOR, 'input[type="submit"]')
    ERRORS = (By.CSS_SELECTOR, ".label.error")


class RegisterPageLocators:
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    PASSWORD2 = (By.NAME, "password2")
    SUBMIT = (By.CSS_SELECTOR, 'input[type="submit"]')

    LOGOUT_BTN = (By.XPATH, '//input[@value="Выйти"]')
    DELETE_BTN = (By.XPATH, '//input[@value="Удалить аккаунт"]')
    DELETE_CONFIRM = (By.ID, "deleteAcc")
    DELETE_SUBMIT = (By.XPATH, '//input[@value="Удалить"]')


class TaskPageLocators:
    ADD_TASK_LINK = (By.LINK_TEXT, "Добавить дело")
    TITLE = (By.ID, "title")
    ADD_BTN = (By.XPATH, '//input[@value="Добавить"]')
    SEARCH = (By.NAME, "search")
    SEARCH_BTN = (By.XPATH, '//input[@value="Найти"]')
