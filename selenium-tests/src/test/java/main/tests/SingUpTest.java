package main.tests;

import main.pages.singUp.SingUpPage;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.PageFactory;

import static main.constants.CommonConstants.*;

public class SingUpTest extends WebDriverSettingsTest {

    @Test
    public void singUp() {

        try {
            SingUpPage singUpPage = PageFactory.initElements(driver, SingUpPage.class);

            singUpPage.openWebPortal();
            singUpPage.waitForm();

            singUpPage.authentication(USER_LOGIN, USER_PASSWORD, USER_CONTRACT);

            singUpPage.waitDashboard();
        }catch (Exception e){
            e.printStackTrace();
        }
    }

    @Test
    public void singUpFailWithNumberOfContract() {

        try {
            SingUpPage singUpPage = PageFactory.initElements(driver, SingUpPage.class);

            singUpPage.openWebPortal();
            singUpPage.waitForm();

            singUpPage.submit();
            singUpPage.waitAlert();

            WebElement alert = singUpPage.getAlert();
            String alertMessage = alert.getText();
            Assert.assertEquals(alertMessage, UNKNOWN_CONTRACT);
        }catch (Exception e){
            e.printStackTrace();
        }
    }

    @Test
    public void singUpFailWithLoginOrPassword() {

        try {
            SingUpPage singUpPage = PageFactory.initElements(driver, SingUpPage.class);

            singUpPage.openWebPortal();
            singUpPage.waitForm();

            singUpPage.typeContract(USER_CONTRACT);
            singUpPage.submit();
            singUpPage.waitAlert();

            WebElement alert = singUpPage.getAlert();
            String alertMessage = alert.getText();
            Assert.assertEquals(alertMessage, LOGIN_OR_PASSWORD_INCORRECT);
        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
