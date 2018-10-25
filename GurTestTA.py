from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://192.168.232.110:8444")

UserPswd = "QWErty123"
def login(driver):
    elem = driver.find_element_by_name("txtLogin").click()
    elem = driver.find_element_by_name("txtLogin").send_keys("admin")
    elem = driver.find_element_by_name("txtPassword").click()
    elem = driver.find_element_by_name("txtPassword").send_keys("Centrex9")
    elem = driver.find_element_by_name("btnLogin").click()
    time.sleep(2)
    elem = driver.find_element_by_xpath('//*[@id="ctl00_NavigationTree_1_0_txt"]').click()
    time.sleep(2)

def create_user(username, password, driver):
    elem = driver.find_element_by_xpath('//*[@id="ctl00_SampleContent_Tabs_pnlUsers_btnAddUserTop"]').click()  # USER ADD
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ctl00_SampleContent_btnSave")))
    elem = driver.find_element_by_xpath('//*[@id="ctl00_SampleContent_Tabs_pnlBaseSettings_txtId"]').send_keys(username)
    elem = driver.find_element_by_xpath('//*[@id="ctl00_SampleContent_Tabs_pnlBaseSettings_txtSubscriberName"]').clear()
    elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlBaseSettings_txtSubscriberName").send_keys(username)
    elem = driver.find_element_by_css_selector( "#ctl00_SampleContent_Tabs_pnlBaseSettings_trRadiusAuthorization .addBlockHeaderWithArrow").click()
    elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlBaseSettings_txtUser").send_keys(username)
    elem = driver.find_element_by_css_selector("#tdGroupSet .addBlockHeaderWithArrow").click()
    options = driver.find_elements_by_css_selector("#ctl00_SampleContent_Tabs_pnlBaseSettings_ucGroups_ddlGroups option")
    for option in options:
        if option.text == 'feature | DialLocalNumbers':
            option.click()
    elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlBaseSettings_ucGroups_btnAddGroup").click()
    time.sleep(1)
    elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlBaseSettings_ucGroups_btnAddGroup").click()
    elem = driver.find_element_by_id("__tab_ctl00_SampleContent_Tabs_pnlServices").click()
    elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlServices_txtWebLogin").clear()
    elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlServices_txtWebLogin").send_keys(username)
    elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlServices_txtWebPassword").clear()
    elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlServices_txtWebPassword").send_keys(username)
    elem = driver.find_element_by_id("__tab_ctl00_SampleContent_Tabs_pnlTerminals").click()
    elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlTerminals_ttTerminals_btnAddNew").click()
    time.sleep(2)
    elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlTerminals_ttTerminals_grdTerminals_ctl01_txtLogin").click()
    elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlTerminals_ttTerminals_grdTerminals_ctl01_txtLogin").send_keys(username)
    elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlTerminals_ttTerminals_grdTerminals_ctl01_txtPassword").click()
    elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlTerminals_ttTerminals_grdTerminals_ctl01_txtPassword").send_keys(password)
    elem = driver.find_element_by_name("ctl00$SampleContent$Tabs$pnlTerminals$ttTerminals$grdTerminals$ctl01$ddlProfile").click()
    options = driver.find_elements_by_css_selector("#ctl00_SampleContent_Tabs_pnlTerminals_ttTerminals_grdTerminals_ctl01_ddlProfile option")
    for option in options:
        if option.text == 'SIP User audio (default)':
            option.click()
    elem = driver.find_element_by_id("ctl00_SampleContent_btnSave").click()
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID , "ctl00_SampleContent_Tabs_pnlUsers_btnAddUserTop")))

def create_users(startNum, endNum, password, driver):
    for number in range(startNum, endNum):
        create_user(number, password, driver)

#Login
login(driver)
#Create users
create_users(4000, 4010, UserPswd, driver)
driver.quit()



