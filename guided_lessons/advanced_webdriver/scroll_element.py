from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ScrollElement():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(4)

        # Scroll Down

        # Scroll Up

        # Scroll Element Into View

        # Native Way To Scroll Element Into View


se = ScrollElement()
se.test()
