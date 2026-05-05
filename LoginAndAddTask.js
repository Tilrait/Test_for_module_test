const { Builder, until, By, revealed } = require("selenium-webdriver");
const { Select } = require("selenium-webdriver");
const chrome = require("selenium-webdriver/chrome");
const assert = require("node:assert");
async function main() {
  const options = new chrome.Options();
  options.windowSize({ width: 1920, height: 1080 });
  const driver = await new Builder()
    .forBrowser("chrome")
    .setChromeOptions(options)
    .build();
  await driver.manage().setTimeouts({ implicit: 3000 });
  let pass;
  let name;
  try {
    await driver.get("http://localhost:8000/");
    async function registration() {
      await driver.findElement(By.linkText("Зарегистрироваться")).click();
      const inp1 = await driver.findElement(By.name("username"));
      const inp2 = await driver.findElement(By.name("password"));
      const inp3 = await driver.findElement(By.name("password2"));
      name = Math.random();
      pass = Math.random();
      await inp1.sendKeys(name);
      await inp2.sendKeys(pass);
      await inp3.sendKeys(pass);
      await driver.findElement(By.css("input[type=submit]")).click();
      const elements = await driver.findElements(
        By.xpath('//input[@value="Выйти"]')
      );
      assert.strictEqual(elements.length, 1, "Не нашел или нашел не то");
      return name;
    }
    async function addWork(taskName) {
      await driver.findElement(By.linkText("Добавить дело")).click();
      const title = await driver.findElement(By.id("title"));
      await title.sendKeys(taskName);
      await driver.findElement(By.xpath('//input[@value="Добавить"]')).click();
      await driver.sleep(1000);
    }
    async function findEl(taskName) {
      const addInfField = await driver.findElement(By.name("search"));
      await addInfField.sendKeys(taskName);
      await driver.findElement(By.xpath('//input[@value="Найти"]')).click();
      const par = await driver.findElement(By.linkText(String(taskName)));
      await driver
        .findElement(
          By.xpath(
            `//a[. = "${taskName}"]/ancestor::article//input[@value="Сделано!"]`,
          ),
        )
        .click();
      const confirms = await driver.findElements(
        By.xpath(
          `//a[. = "${taskName}"]/ancestor::article//input[@value="Сделано!"]`,
        ),
      );
      assert.strictEqual(confirms.length, 0, "Дело не сделано или не добавлено");
      await driver.sleep(2000);
    }
    const registeredName = await registration();
    await addWork(registeredName);
    await findEl(registeredName);
  } catch (err) {
    console.log(err);
  } finally {
    await driver.sleep(5000);
    await driver
      .findElement(By.xpath('//input[@value="Удалить аккаунт"]'))
      .click();
    const confDel = await driver.findElement(By.id("deleteAcc"));
    await confDel.sendKeys(pass);
    await driver.findElement(By.xpath('//input[@value="Удалить"]')).click();
    await driver.quit();
  }
}
main().catch(console.error);