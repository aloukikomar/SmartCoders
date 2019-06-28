from selenium import webdriver
import time

#------| Code use to logout user#

def logout(driver):
    try:
        element=driver.find_element_by_xpath("//li[@id='logout']//a")
        element.click()
        time.sleep(2)
        return 1
    except:
        return 0   