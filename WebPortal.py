from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random

chislo = random.randint(1000, 9999)
AbonentInfo = "Test" + str(chislo)

#Open Browser, Get login Page
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://192.168.232.115")

#Login Page
def login(driver):
    elem = driver.find_element_by_name("login").click()
    elem = driver.find_element_by_name("login").send_keys("Gtest0001")
    elem = driver.find_element_by_name("password").click()
    elem = driver.find_element_by_name("password").send_keys("QWErty123")
    elem = driver.find_element_by_name("contract").click()
    elem = driver.find_element_by_name("contract").send_keys("Gtest0001")
    elem = driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/form/div[4]/button").click()
    wait = WebDriverWait(driver, 15)
    elem = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-layout/div/div/header/app-navbar/nav/div/div[2]/ul/li[3]/a/span')))

#Create Abon
def create_abon(info, driver):
    elem = driver.find_element_by_xpath("/html/body/app-root/app-layout/div/div/header/app-navbar/nav/div/div[2]/ul/li[3]/a/span").click()
    elem = driver.find_element_by_xpath("/html/body/app-root/app-layout/div/div/div/app-employee-list/div/div[2]/card/div/div[3]/card-footer/div/button").click()
    elem = driver.find_element_by_id("name").click()
    elem = driver.find_element_by_id("name").send_keys(info)
    elem = driver.find_element_by_id("email").click()
    elem = driver.find_element_by_id("email").send_keys(info+"@test.ru")
    elem = driver.find_element_by_id("login").click()
    elem = driver.find_element_by_id("login").send_keys(info)
    elem = driver.find_element_by_xpath("/html/body/app-root/app-layout/div/div/div/app-employee-detail/div/div/card/div/div[2]/card-body/div/app-personal/form/div[1]/div[2]/div[1]/div/p-autocomplete/span/input").click()
    elem = driver.find_element_by_xpath("/html/body/app-root/app-layout/div/div/div/app-employee-detail/div/div/card/div/div[2]/card-body/div/app-personal/form/div[1]/div[2]/div[1]/div/p-autocomplete/span/input").send_keys(chislo)
    elem = driver.find_element_by_id("password").click()
    elem = driver.find_element_by_id("password").clear()
    elem = driver.find_element_by_id("password").send_keys(info)
    elem = driver.find_element_by_id("passwordConfirm").click()
    elem = driver.find_element_by_id("passwordConfirm").clear()
    elem = driver.find_element_by_id("passwordConfirm").send_keys(info)
    elem = driver.find_element_by_id("termPass").click()
    elem = driver.find_element_by_id("termPass").clear()
    elem = driver.find_element_by_id("termPass").send_keys(info)
    elem = driver.find_element_by_xpath("/html/body/app-root/app-layout/div/div/div/app-employee-detail/div/div/card/div/div[2]/card-body/div/app-personal/form/div[3]/div/button[2]").click()
    wait = WebDriverWait(driver, 15)
    elem = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-layout/div/div/div/app-employee-detail/div/div/card/div/div[2]/card-body/div/app-personal/form/div[2]/div/p-accordion/div/p-accordiontab[1]/div[1]/a/p-header/span')))
    elem = driver.find_element_by_xpath("/html/body/app-root/app-layout/div/div/header/app-navbar/nav/div/div[2]/ul/li[3]/a/span").click()



login(driver)
create_abon(AbonentInfo, driver)
time.sleep(5)
driver.quit()
