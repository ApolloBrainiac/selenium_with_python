from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class WindowSize():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.implicitly_wait(5)


        height = ""
        width = ""
        print("Height: " + str(height))
        print("Width: " str(width))

        time.sleep(3)
        driver.quit()


ws = WindowSize()
ws.test()
