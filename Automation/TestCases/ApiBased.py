import requests,time
from HelperFunctions.AddToCart import ATK
from Config import SetDriver ,data

def mainApiCart():
    Result=0
    CofigData =data()
    try:
        #------|open chrome web driver and hit given product url#
        driver=SetDriver("Chrome")
        if driver == "error":
            return Result
        driver.get("http://"+CofigData.localhost+"/detail.html?id=510a0d7e-8e83-4193-b483-e27e09ddc34d")
        time.sleep(3)

        #-----|get current cart#
        response1 = requests.get('http://172.22.0.1/cart')
        #print(response.text)
        if ATK(driver) == 0:
            return Result

        #-----|get current cart#
        response2 = requests.get('http://172.22.0.1/cart')
        if response1.text == response2.text:
            return Result
        Result=1
    except:
        print("error")
    return Result