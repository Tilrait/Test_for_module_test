const { Builder } = require("selenium-webdriver");
const assert = require("assert");

let driver;

function getBrowser() {
  const browserName = process.env.BROWSER || "chrome";

  return new Builder().forBrowser(browserName).build();
}

describe("Browser fixture example", function () {
  this.timeout(30000);

  before(async function () {
    driver = await getBrowser();
  });

  beforeEach(async function () {
  });

  after(async function () {
    if (driver) {
      await driver.quit();
    }
  });

  it("Example test", async function () {
    await driver.get("https://example.com");
  });
});