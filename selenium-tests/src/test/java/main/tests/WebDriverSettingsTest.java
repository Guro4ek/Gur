package main.tests;

import org.junit.After;
import org.junit.Before;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeDriverService;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.File;

public class WebDriverSettingsTest {

    public ChromeDriver driver;
    public WebDriverWait wait;

    @Before
    public void openWebPortalPage() {
        ChromeDriverService service = new ChromeDriverService.Builder()
                .usingDriverExecutable(new File("src/main/resources/drivers/v2.42/chromedriver"))
                .usingAnyFreePort()
                .build();

        DesiredCapabilities caps = DesiredCapabilities.chrome();
        caps.setCapability(CapabilityType.ACCEPT_SSL_CERTS, true);
        caps.setCapability(CapabilityType.ACCEPT_INSECURE_CERTS, true);
        ChromeOptions chromeOptions = new ChromeOptions();
//        chromeOptions.addArguments("--headless");
        caps.setCapability(ChromeOptions.CAPABILITY, chromeOptions );
        chromeOptions.merge(caps);
        driver = new ChromeDriver(service, chromeOptions);
    }

    @After
    public void closeWebPortalPage() {
        driver.quit();
    }
}
