from selenium import webdriver
import time
from Config import SetDriver ,data

def mainCr():
    Result=0
    CofigData =data()
    try:
        #------|open chrome web driver and hit Home Page#
        driver=SetDriver("Chrome")
        if driver == "error":
            return Result
        driver.get("http://"+CofigData.localhost)
        time.sleep(3)

        #------|Get and verify title#
        if driver.title == "WeaveSocks":

        #print(element)
            return 1
    except:
        print("error")
    return Result