package Page;

import org.openqa.selenium.By;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class UserPage extends SecuredPage {

    @FindBy(id = "name")
    private WebElement nameField;

    @FindBy(id = "email")
    private WebElement emailField;

    //@FindBy(id = "cellNumber")
    //private WebElement cellNumberField;

    @FindBy(id = "login")
    private WebElement loginField;

    @FindBy(id = "password")
    private WebElement passwordField;

    @FindBy(id = "passwordConfirm")
    private WebElement passwordConfirmField;

    @FindBy(id = "termPass")
    private WebElement termPassField;

    @FindBy(css = "[type=\"submit\"]")//(id = "saveUserBtn")
    private WebElement saveUserBtn;

    @FindBy(css = "div.row:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(3) > button:nth-child(1)")
    private WebElement randNumberBtn;

    @FindBy(css = "span[title=\"Atest1234\"]")
    private WebElement createdUser;

    @FindBy(css = ".btn-danger")
    private WebElement deleteUserBtn;

    @FindBy(css = ".col-md-9 > card:nth-child(1) > div:nth-child(1) > div:nth-child(3) > card-footer:nth-child(1) > div:nth-child(1) > button:nth-child(1)")
    private WebElement addUserBtn;

    public UserPage(WebDriver driver) {
        super(driver);
    }

    public void createUser() {
        addUserBtn.click();
        nameField.sendKeys("Atest1234");
        emailField.sendKeys("Atest1234@test.ru");
        loginField.sendKeys("Atest1234");
        //cellNumberField.sendKeys("9123456780");
        randNumberBtn.click();
        passwordField.clear();
        passwordField.sendKeys("Atest1234");
        passwordConfirmField.clear();
        passwordConfirmField.sendKeys("Atest1234");
        termPassField.clear();
        termPassField.sendKeys("Atest1234");
        saveUserBtn.click();
        WebDriverWait waitDashboard = new WebDriverWait(driver, 20);
        waitDashboard.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".btn-danger")));
        //waitDashboard.until(ExpectedConditions.visibilityOf(deleteUserBtn));
    }

    public void deleteUser() {
        createdUser.click();
        deleteUserBtn.click();
        WebDriverWait waitDashboard = new WebDriverWait(driver, 20);
        waitDashboard.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".col-md-9 > card:nth-child(1) > div:nth-child(1) > div:nth-child(3) > card-footer:nth-child(1) > div:nth-child(1) > button:nth-child(1)")));
        //waitDashboard.until(ExpectedConditions.visibilityOf(addUserBtn));
    }

}
