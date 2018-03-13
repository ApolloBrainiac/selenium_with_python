from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DropDown():
    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        print("Select Benz by value")

        time.sleep(2)

        print("Select Honda by index")

        time.sleep(2)

        print("Select BMW by visible text")

        time.sleep(2)

        print("Select Honda by index")

dd = DropDown()
dd.test()
