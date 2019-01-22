package Page;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class SecuredPage extends Page {

    @FindBy(css = "[href=\"/employees\"]")
    WebElement usersNav;

    @FindBy(css = "li.dropdown:nth-child(7) > a:nth-child(1) > span:nth-child(2)")
    WebElement profileNav;

    @FindBy(css = "li.dropdown:nth-child(7) > ul:nth-child(2) > li:nth-child(7) > a:nth-child(1)")
    WebElement logoutBtn;

    //@FindBy(css = "[type=\"submit\"]")
    //WebElement loginBtn;

    public SecuredPage(WebDriver driver) {
        super(driver);
    }

    public void goToUserPage(){
        usersNav.click();
    }

    public void logOut(){
        profileNav.click();
        logoutBtn.click();
        WebDriverWait waitDashboard = new WebDriverWait(driver, 20);
        waitDashboard.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector("[type=\"submit\"]")));
        //waitDashboard.until(ExpectedConditions.visibilityOf(loginBtn));
    }
}
