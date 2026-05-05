    // удаление аккаунта
    

    // проверить что отметилось как выполненное

    //   const price = await driver.findElement(By.id("price"))
    //   await driver.wait(until.elementTextIs(price,"$100"), 15000);

    //   const button = await driver.findElement(By.id("book"));
    //   button.click()

    // await driver.wait(until.elementIsEnabled(button), 2000);

    // button.click();

    // const window = await driver.getAllWindowHandles()
    // await driver.switchTo().window(window[1]);

    // const inp = await driver.findElement(By.id("answer"))
    // const x = await driver.findElement(By.id("input_value")).getText();
    // await inp.sendKeys(String(Math.log(Math.abs(Math.sin(+x) * 12))));

    // const lastButtonSubmit = await driver.findElement(By.className("btn"))
    // await lastButtonSubmit.click();

    // const buttonSubmit = await driver.findElement(By.className("btn"));

    // await driver.executeScript(
    //   "return arguments[0].scrollIntoView(true)",
    //   buttonSubmit
    // );
    // await buttonSubmit.click()

    // const el1 = await driver.findElement(By.id("num1"));
    // const el2 = await driver.findElement(By.id("num2"));

    // const res = +(await el1.getText()) + +(await el2.getText());

    // const select = new Select(await driver.findElement(By.id("dropdown")));
    // await select.selectByValue(String(res));

    // const buttonSubmit = await driver.findElement(By.className("btn"))
    // await buttonSubmit.click()

    // const chest = await driver.findElement(By.id("treasure"));

    // const res = await chest.getAttribute("valuex");

    // const inp = await driver.findElement(By.id("answer"));
    // await inp.sendKeys(String(Math.log(Math.abs(Math.sin(+res) * 12))));

    // const robotsCheckBox = await driver.findElement(By.id("robotCheckbox")).click();

    // const robots_rule = await driver.findElement(By.id("robotsRule")).click();

    // const submitButton = await driver.findElement(By.className("btn"));
    // await submitButton.click();

    // robot_checkBox = await driver.findElement(By.id("robotCheckBox"));
    // robots_rule = await driver.findElement(By.id("robotsRule"));
    // people_rule = await driver.findElement(By.id("peopleRule"));

    // await assert.strictEqual()

    // const findSome = await driver.findElement(
    //   By.xpath('//input[@required]')
    // );
    //  await findSome.click();

    // for (let el of await driver.findElements(By.css("input[required]"))) {
    //   await el.sendKeys("Tarkov Citizen");
    // }

    // const buttonSubmit = await driver.findElement(By.xpath("//button[text()='Submit']"))

    // await buttonSubmit.click();

    // const welcome_text = await driver.findElement(By.css("h1")).getText()
    // assert.strictEqual(
    //   welcome_text, "Congratulations! You have successfully registered!"
    // );

    // Поиск find link text

    // const result = Math.ceil(Math.pow(Math.PI, Math.E) * 10000);
    // const findLink = await driver.findElement(By.linkText(result.toString()));

    // await findLink.click()

    // Поиск элемента textarea

    // for (let el of findSome) {
    //   await el.sendKeys("TARKOV CITIZEN")
    // }
    // const textarea1 = await driver.findElement(By.name("first_name"));
    // await textarea1.sendKeys("GOYDA");

    // const textarea2 = await driver.findElement(By.name("last_name"));
    // await textarea2.sendKeys("GOYDA");

    // const textarea3 = await driver.findElement(
    //   By.className("form-control city")
    // );
    // await textarea3.sendKeys("GOYDA");

    // const textarea4 = await driver.findElement(By.id("country"));
    // await textarea4.sendKeys("GOYDA");

    // Поиск и клик по кнопке submit
    // const submitButton = await driver.findElement(By.className("btn-default"));
    // await submitButton.click();