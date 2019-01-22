package Page;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class LoginPage extends Page {

    @FindBy(name = "login")
    private WebElement loginField;

    @FindBy(name = "password")
    private WebElement passwordField;

    @FindBy(name = "contract")
    private WebElement contractField;

    @FindBy(css = "[type=\"submit\"]")
    private WebElement loginButton;

    public LoginPage(WebDriver driver) {
        super(driver);
    }

    public void login(String name, String password, String contract) {
        loginField.click();
        loginField.sendKeys(name);
        passwordField.click();
        passwordField.sendKeys(password);
        contractField.click();
        contractField.sendKeys(contract);
        loginButton.click();
        WebDriverWait waitDashboard = new WebDriverWait(driver, 20);
        waitDashboard.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector("[href=\"/employees\"]")));
    }
}
