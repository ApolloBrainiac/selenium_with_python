from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class MouseHover():

    def test(self):
        baseUrl = ""
        driver = webdriver.Firefox()
        driver.maximize_window
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        element = driver.find_element(
            By.ID, "")
        element.click()
        time.sleep(4)


mh = MouseHover()
mh.test()
