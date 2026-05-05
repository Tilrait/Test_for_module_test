const { Builder } = require("selenium-webdriver");
const assert = require("assert");

let driver;

function getBrowser() {
  const browserName = process.env.BROWSER || "chrome";

  return new Builder().forBrowser(browserName).build();
}

describe("Example test", function () {
  this.timeout(30000);

  before(async function () {
    driver = await getBrowser();
  });

  after(async function () {
    if (driver) {
      await driver.quit();
    }
  });

  it("Open Google and check title", async function () {
    await driver.get("https://www.google.com");

    const title = await driver.getTitle();
    assert.ok(title.includes("Google"));
  });
});