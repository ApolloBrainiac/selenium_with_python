from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class autoComplete():

    def test(self):
        baseUrl = "https://www.southwest.com"
        driver = webdriver.Firefox()
        driver.maximize_window
        driver.get(baseUrl)
        driver.implicitly_wait(4)

        element = driver.find_element(By.ID, "")
        element.click()

        time.sleep(2)


ac = autoComplete()
ac.test()
