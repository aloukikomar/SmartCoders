from selenium import webdriver
import time

#------| Code used to login wit user : user and password : password#

def login(driver,user,password):
    try:
        element=driver.find_element_by_xpath("//li[@id='login']//a[text()='Login']")
        element.click()
        time.sleep(2)
        element=driver.find_element_by_xpath("//input[@id='username-modal']")
        element.clear()
        element.send_keys(user)
        element=driver.find_element_by_xpath("//input[@id='password-modal']")
        element.clear()
        element.send_keys(password)
        element=driver.find_element_by_xpath("//button[@onclick='return login()']")
        element.click()
        time.sleep(5)
        return 1
    except:
        return 0   