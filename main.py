from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOption
import time

ChromeOption = ChromeOption()
driver = webdriver.Remote(
    command_executor="http://10.11.19.123:4444", options=ChromeOption
)

try:
    driver.get("https://google.com")
    driver.find_element(By.NAME, "q").send_keys("Selenium Grid")
finally:
    time.sleep(5)
    driver.quit()
