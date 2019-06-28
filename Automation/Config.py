from selenium import webdriver
from selenium.webdriver.chrome.options import Options
class data():
    localhost="172.22.0.1"

def SetDriver(DriverOption):
    if DriverOption == "Chrome":
        options = Options()
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')  # Last I checked this was necessary.
        options.add_argument('--disable-dev-shm-usage')
        driver=webdriver.Chrome(executable_path="Drivers/chromedriver",chrome_options=options)
        driver.set_window_size(1800, 1000)
        return driver
    return "error"