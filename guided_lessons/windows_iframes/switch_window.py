from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchWindow():
    
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practic"
        driver = webdriver.Firefox()
        driver.maximize_window
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        # Find parent handle -> Main Window

        # Find open window button and click it

        # Find all handles, there should be two handles after clicking open window button

        # Switch to window and search course


        # Switch back to the parent handle


sw = SwitchWindow()
sw.test()
