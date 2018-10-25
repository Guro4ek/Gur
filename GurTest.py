from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://192.168.232.110:8444")

UserName = 4000
UserPswd = "QWErty123"
#Login
elem = driver.find_element_by_name("txtLogin").click()
elem = driver.find_element_by_name("txtLogin").send_keys("admin")
elem = driver.find_element_by_name("txtPassword").click()
elem = driver.find_element_by_name("txtPassword").send_keys("Centrex9")
elem = driver.find_element_by_name("btnLogin").click()
time.sleep(3)
#Root
elem = driver.find_element_by_xpath('//*[@id="ctl00_NavigationTree_1_0_txt"]').click()
time.sleep(3)

elem = driver.find_element_by_xpath('//*[@id="ctl00_SampleContent_Tabs_pnlUsers_btnAddUserTop"]').click() #USER ADD
time.sleep(3)
elem = driver.find_element_by_xpath('//*[@id="ctl00_SampleContent_Tabs_pnlBaseSettings_txtId"]').send_keys(UserName)
elem = driver.find_element_by_xpath('//*[@id="ctl00_SampleContent_Tabs_pnlBaseSettings_txtSubscriberName"]').clear()
elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlBaseSettings_txtSubscriberName").send_keys(UserName)
elem = driver.find_element_by_css_selector("#ctl00_SampleContent_Tabs_pnlBaseSettings_trRadiusAuthorization .addBlockHeaderWithArrow").click()
elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlBaseSettings_txtUser").send_keys(UserName)
elem = driver.find_element_by_xpath("//form/table[1]/tbody/tr[2]/td/div/table/tbody/tr/td[2]/table/tbody/tr[5]/td/table/tbody/tr[2]/td[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[5]/td/div/a").click()
elem = driver.find_element_by_xpath('//*[@id="ctl00_SampleContent_Tabs_pnlBaseSettings_ucGroups_ddlGroups"]').click()
elem = driver.find_element_by_name("ctl00$SampleContent$Tabs$pnlBaseSettings$ucGroups$ddlGroups").click()
elem = driver.find_element_by_xpath("//form/table[1]/tbody/tr[2]/td/div/table/tbody/tr/td[2]/table/tbody/tr[5]/td/table/tbody/tr[2]/td[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[5]/td/div/div/div/center/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[2]/td[1]/select/option[15]").click()
elem = driver.find_element_by_name("ctl00$SampleContent$Tabs$pnlBaseSettings$ucGroups$btnAddGroup").click()
elem = driver.find_element_by_name("ctl00$SampleContent$Tabs$pnlBaseSettings$ucGroups$btnAddGroup").click()
elem = driver.find_element_by_id("__tab_ctl00_SampleContent_Tabs_pnlServices").click()
elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlServices_txtWebLogin").clear()
elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlServices_txtWebLogin").send_keys(UserName)
elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlServices_txtWebPassword").clear()
elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlServices_txtWebPassword").send_keys(UserPswd)
elem = driver.find_element_by_id("__tab_ctl00_SampleContent_Tabs_pnlTerminals").click()
elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlTerminals_ttTerminals_btnAddNew").click()
time.sleep(3)
elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlTerminals_ttTerminals_grdTerminals_ctl01_txtLogin").click()
elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlTerminals_ttTerminals_grdTerminals_ctl01_txtLogin").send_keys(UserName)
elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlTerminals_ttTerminals_grdTerminals_ctl01_txtPassword").click()
elem = driver.find_element_by_id("ctl00_SampleContent_Tabs_pnlTerminals_ttTerminals_grdTerminals_ctl01_txtPassword").send_keys(UserPswd)
elem = driver.find_element_by_name("ctl00$SampleContent$Tabs$pnlTerminals$ttTerminals$grdTerminals$ctl01$ddlProfile").click()
elem = driver.find_element_by_xpath("//form/table[1]/tbody/tr[2]/td/div/table/tbody/tr/td[2]/table/tbody/tr[5]/td/table/tbody/tr[2]/td[2]/div[1]/div[2]/div[3]/div/table[1]/tbody/tr[2]/td[7]/table/tbody/tr[1]/td[2]/select/option[6]").click()
elem = driver.find_element_by_id("ctl00_SampleContent_btnSave").click()
time.sleep(3)
driver.close()

