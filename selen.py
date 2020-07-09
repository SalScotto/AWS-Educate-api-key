from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

from creds import username, password

awsEducateLogin = "https://www.awseducate.com/signin/SiteLogin"
classroomUrl = "https://www.awseducate.com/student/s/classrooms"

xPaths = {
    'usernameField' : '//*[@id="loginPage:siteLogin:loginComponent:loginForm:username"]',
    'passwordField' : '//*[@id="loginPage:siteLogin:loginComponent:loginForm:password"]',
    'loginButton' : '/html/body/span[1]/form/span/div/div/div/div[2]/div/p/a',
    'myClassroom' : '/html/body/div[3]/div[1]/div/nav/div/div[2]/ul/li[1]/a',
    'goToFirstClass': '/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/table/tbody/tr[1]/td[6]/div[2]/a',
    'continue': '/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div/div[3]/button[1]',
    'showDetails': '//*[@id="showawsdetail"]',
    'unhide': '//*[@id="clikeyboxbtn"]',
    'keys': '/html/body/div[1]/div[2]/div/div/div[21]/div[2]/p/div/pre/span'
}

print("Initializing Selenium...")
driver = webdriver.Firefox()
try:
    driver.get(awsEducateLogin)
    driver.implicitly_wait(15)

    userField = driver.find_element_by_xpath(xPaths['usernameField'])
    userField.send_keys(username)
    sleep(0.1)
    pwField = driver.find_element_by_xpath(xPaths['passwordField'])
    pwField.send_keys(password)
    sleep(0.1)
    butt = driver.find_element_by_xpath(xPaths['loginButton'])
    butt.click()
    sleep(6)

    driver.get(classroomUrl)
    sleep(2)

    driver.find_element_by_xpath(xPaths['goToFirstClass']).click()
    driver.find_element_by_xpath(xPaths['continue']).click()
    sleep(2)

    workbenchTab = driver.window_handles[-1]
    driver.switch_to.window(workbenchTab)
    sleep(2)

    driver.find_element_by_xpath(xPaths['showDetails']).click()
    sleep(2)

    driver.find_element_by_xpath(xPaths['unhide']).click()
    sleep(0.2)
    
    keys = driver.find_element_by_xpath(xPaths['keys']).text
    print(keys)

except Exception as e:
    print("Feeeeeeeeeeeeeeerm")
    print(e)

finally:
    driver.quit()