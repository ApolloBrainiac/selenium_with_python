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

        # Switch to frame using Id
        driver.switch_to.frame("courses-iframe")

        # Switch to frame using name

        # Switch to frame using numbers

        time.sleep(4)
        # Search course
        searchBox = driver.find_element(
            By.ID, "search-courses")
        searchBox.send_keys("python")
        time.sleep(4)

        # Switch back to the parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(4)
        driver.find_element(By.ID, "name").send_keys("Test Successful")

fs = FrameSwitch()
fs.test()
