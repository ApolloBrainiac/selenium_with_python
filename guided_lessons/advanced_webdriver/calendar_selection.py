from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class calendarSelect():

    def test(self):
        baseUrl = ""
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)


cs = calendarSelect()
cs.test()
