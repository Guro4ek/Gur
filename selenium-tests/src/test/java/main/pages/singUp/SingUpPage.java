package main.pages.singUp;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import static main.constants.CommonConstants.WEB_PORTAL_URL;

public class SingUpPage {

    @FindBy(name = "login")
    private WebElement login;

    @FindBy(name = "password")
    private WebElement password;

    @FindBy(name = "contract")
    private WebElement contract;

    @FindBy(css = "[type=\"submit\"]")
    private WebElement submitButton;

    private By alertLocator = By.cssSelector(".alert-body");
    private By dashboardLocator = By.cssSelector("[href=\"/dashboard\"]");
    private By formLocator = By.tagName("form");

    private WebDriver driver;
    private WebDriverWait wait;

    public SingUpPage(){
    }

    public SingUpPage(WebDriver driver){
        this.driver = driver;
        this.wait = new WebDriverWait(driver, 20);
    }

    public void openWebPortal() {
        driver.get(WEB_PORTAL_URL);
    }

    public SingUpPage authentication(String userLogin, String userPassword, String userContract) {
        typeUsername(userLogin);
        typePassword(userPassword);
        typeContract(userContract);
        submit();
        return new SingUpPage(driver);
    }

    public SingUpPage typeUsername(String userLogin) {
        login.sendKeys(userLogin);
        return this;
    }

    public SingUpPage typePassword(String userPassword) {
        password.sendKeys(userPassword);
        return this;
    }

    public SingUpPage typeContract(String userContract) {
        contract.sendKeys(userContract);
        return this;
    }

    public SingUpPage submit() {
        submitButton.click();
        return new SingUpPage(driver);
    }

    public WebElement getAlert() {
        return driver.findElement(alertLocator);
    }

    public void waitForm() {
        wait.until(ExpectedConditions.visibilityOfElementLocated(formLocator));
    }

    public void waitDashboard() {
        wait.until(ExpectedConditions.visibilityOfElementLocated(dashboardLocator));
    }

    public void waitAlert() {
        wait.until(ExpectedConditions.visibilityOfElementLocated(alertLocator));
    }
}
