const { Builder, until, By, revealed } = require("selenium-webdriver");
const { Select } = require("selenium-webdriver");
const chrome = require("selenium-webdriver/chrome");
const assert = require("node:assert");
const { getRandomValues } = require("node:crypto");

async function main() {
  const options = new chrome.Options();
  options.windowSize({ width: 1920, height: 1080 });

  // Создание драйвера
  const driver = await new Builder()
    .forBrowser("chrome")
    .setChromeOptions(options)
    .build();
  try {
    await driver.get("http://localhost:8000/");

    const notLog = await driver
      .findElement(By.className("button success"))
      .click();

    const inp1 = await driver.findElement(By.name("username"));
    const inp2 = await driver.findElement(By.name("password"));

    const name = Math.random();
    const pass = Math.random();

    await inp1.sendKeys(name);
    await inp2.sendKeys(pass);

    const button = await driver
      .findElement(By.css("input[type=submit]"))
      .click();

    const errors = await driver.findElements(By.css(".label.error"));
    assert.ok(errors.length <= 1, "Почему-то зашли хотя не должны");
      
  } catch (err) {
    console.error(err);
  } finally {
    await driver.sleep(10000);
    // Закрытие браузера
    await driver.quit();
  }
}

main().catch(console.error);
