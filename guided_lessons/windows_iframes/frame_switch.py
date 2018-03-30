from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class FrameSwitch():

    def test(self):
        baseUrl = ""
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        driver.execute_script("window.scrollBy(0, 1000);")

        element = driver.find_element(
            By.ID, "")
        element.click()
        time.sleep(4)

        # Switch to frame using Id

        # Switch to frame using name

        # Switch to frame using numbers

        # Search course

        # Switch back to the parent handle


fs = FrameSwitch()
fs.test()
