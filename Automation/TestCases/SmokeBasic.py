from selenium import webdriver
from HelperFunctions.Login import login
from HelperFunctions.Logout import logout
from HelperFunctions.AddToCart import ATK
import time
from Config import SetDriver ,data

#------| Test case to check integration of add to cart feature from UI #

def mainSmBS():
    Result=0
    CofigData =data()
    try:
        #------|open chrome web driver and hit given product url#
        driver=SetDriver("Chrome")
        if driver == "error":
            return Result
        driver.get("http://"+CofigData.localhost+"/detail.html?id=510a0d7e-8e83-4193-b483-e27e09ddc34d")
        time.sleep(3)

        #------|login#
        if login(driver,"user","password") == 0:
            return Result
        #------|add to cart#
        #driver.save_screenshot("SendData.png")
        if ATK(driver) == 0:
            return Result
        else:
            #------|if result is positive #
            Result=1
        #------|logout#
        if logout(driver) == 0:
            return 0
    except:
        print("error")
    return Result