package main.tests;

import Page.LoginPage;
import Page.SecuredPage;
import Page.UserPage;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.util.concurrent.TimeUnit;
import org.junit.FixMethodOrder;
import org.junit.runners.MethodSorters;
@FixMethodOrder(MethodSorters.NAME_ASCENDING)

public class Gurin {

    private static WebDriver driver;

    @BeforeClass
    public static void setup() {
        System.setProperty("webdriver.chrome.driver", "C:\\Java_WP\\selenium-tests\\src\\main\\resources\\drivers\\v2.42\\chromedriver.exe");
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        driver.get("https://192.168.232.175");
    }

    @Test
    public void Alogin() {
        LoginPage loginPage = new LoginPage(driver);
        loginPage.login("WpGurDom1", "WpGurDom1","WpGurDom1");
    }

    @Test
    public void Buser() {
        SecuredPage securedPage = new SecuredPage(driver);
        UserPage userPage = new UserPage(driver);
        securedPage.goToUserPage();
        userPage.createUser();
        securedPage.goToUserPage();
        userPage.deleteUser();
    }

    @AfterClass
    public static void tearDown() {
        SecuredPage securedPage = new SecuredPage(driver);
        securedPage.logOut();
        driver.quit();
    }
}

