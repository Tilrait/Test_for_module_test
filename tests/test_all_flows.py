import random

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "http://localhost:8000/"


class TestFlows:
    @pytest.mark.parametrize(
        "username,password",
        [
            ("123", "Tilrait"),
            ("Egoref", "123"),
            ("Tilrait", "123"),
        ],
    )
    def test_login(self, browser, username, password):
        browser.get(BASE_URL)

        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button.success"))).click()

        inp1 = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        inp2 = browser.find_element(By.NAME, "password")
        inp1.send_keys(username)
        inp2.send_keys(password)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"]'))).click()

        errors = browser.find_elements(By.CSS_SELECTOR, ".label.error")
        assert len(errors) <= 1

    def test_invalid_login(self, browser):
        browser.get(BASE_URL)

        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button.success"))).click()

        inp1 = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        inp2 = browser.find_element(By.NAME, "password")
        inp1.send_keys(str(random.random()))
        inp2.send_keys(str(random.random()))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"]'))).click()

        errors = browser.find_elements(By.CSS_SELECTOR, ".label.error")
        assert len(errors) >= 1

    def test_registration(self, browser):
        browser.get(BASE_URL)
        wait = WebDriverWait(browser, 10)

        name = "user_" + str(random.randint(1, 1_000_000))
        password = "pass_" + str(random.randint(1, 1_000_000))

        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться"))).click()

        inp1 = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        inp2 = browser.find_element(By.NAME, "password")
        inp3 = browser.find_element(By.NAME, "password2")

        inp1.send_keys(name)
        inp2.send_keys(password)
        inp3.send_keys(password)

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"]'))).click()

        logout_buttons = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, '//input[@value="Выйти"]'))
        )
        assert len(logout_buttons) == 1

        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Удалить аккаунт"]'))).click()
        conf_del = wait.until(EC.presence_of_element_located((By.ID, "deleteAcc")))
        conf_del.send_keys(password)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Удалить"]'))).click()

    def test_add_task(self, browser):
        browser.get(BASE_URL)
        wait = WebDriverWait(browser, 10)

        name = "task_user_" + str(random.randint(1, 1_000_000))
        password = "password123"
        task_name = "Купить хлеб"

        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться"))).click()

        inp1 = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        inp2 = browser.find_element(By.NAME, "password")
        inp3 = browser.find_element(By.NAME, "password2")

        inp1.send_keys(name)
        inp2.send_keys(password)
        inp3.send_keys(password)

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"]'))).click()

        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Добавить дело"))).click()
        title = wait.until(EC.presence_of_element_located((By.ID, "title")))
        title.send_keys(task_name)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Добавить"]'))).click()

        search = wait.until(EC.presence_of_element_located((By.NAME, "search")))
        search.send_keys(task_name)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Найти"]'))).click()

        done_button_xpath = (
            f'//a[. = "{task_name}"]/ancestor::article//input[@value="Сделано!"]'
        )
        wait.until(EC.element_to_be_clickable((By.XPATH, done_button_xpath))).click()
        wait.until(EC.invisibility_of_element_located((By.XPATH, done_button_xpath)))
        confirms = browser.find_elements(By.XPATH, done_button_xpath)
        assert len(confirms) == 0

        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Удалить аккаунт"]'))).click()
        conf_del = wait.until(EC.presence_of_element_located((By.ID, "deleteAcc")))
        conf_del.send_keys(password)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Удалить"]'))).click()
