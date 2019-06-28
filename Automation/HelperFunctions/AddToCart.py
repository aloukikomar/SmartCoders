from selenium import webdriver
import time

#------| Code used to add product in the cart#

def ATK(driver):
    #try:
        #print(driver.find_elements_by_xpath("//*")[0].text)
        element=driver.find_element_by_xpath("//span[@id='numItemsInCart']")
        #------|get initial cart item value #
        initialVal = int(element.text.split(" ")[0])
        element=driver.find_element_by_xpath("//a[@id='buttonCart']")
        element.click()
        time.sleep(3)
        element=driver.find_element_by_xpath("//span[@id='numItemsInCart']")
        #------|get final cart item value #
        finalVal = int(element.text.split(" ")[0])
        #------|Check if incremented by one #
        if initialVal == finalVal -1:
            return 1
        return 0
    #except:
        return 0   