from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class javaScriptExecute():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        element = driver.find_element(
            By.ID, "")
        element.click()

        time.sleep(3)
        driver.quit()


js = javaScriptExecute()
js.test()
