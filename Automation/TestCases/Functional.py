from selenium import webdriver
import time
from HelperFunctions.AddToCart import ATK
from Config import SetDriver ,data

#------| Test case for smoke test of add to cart feature from UI #

def mainFn():
    Result=0
    CofigData =data()
    try:
        #------|open chrome web driver and hit given product url#
        driver=SetDriver("Chrome")
        if driver == "error":
            return Result
        driver.get("http://"+CofigData.localhost+"/detail.html?id=510a0d7e-8e83-4193-b483-e27e09ddc34d")
        time.sleep(3)
        
        if ATK(driver) == 0:
            return Result
        else:
            #------|if result is positive #
            Result=1
    except:
        print("error")
    return Result