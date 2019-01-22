package main.pages.dashboard;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;

public class DashboardPage {

    private WebDriver driver;
    private WebDriverWait wait;

    public DashboardPage(){
    }

    public DashboardPage(ChromeDriver driver){
        this.driver = driver;
        this.wait = new WebDriverWait(driver, 10);
    }
}