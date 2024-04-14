# Selenium Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


# Time Library Import
import time

# Configuring Webdriver
driver = webdriver.Chrome()

# Reusable Function Declaration
def delay(seconds=1):
    time.sleep(seconds)

# Test Site
url = 'http://www.google.com/'
driver.get(url)
driver.maximize_window()

# Object Repository
search_box = element = driver.find_element(By.NAME, "q")

# script
driver.implicitly_wait(10)
print("Page Loaded")
search_box.send_keys('times', Keys.META)
search_box.submit()
print("Searched")

delay(20)
driver.quit()