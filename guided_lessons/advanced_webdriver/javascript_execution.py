from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class javaScriptExecute():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window
        # driver.get(baseUrl)
        driver.execute_script(
            "window.location = 'https://letskodeit.teachable.com/pages/practice';")
        driver.implicitly_wait(5)

        time.sleep(3)
        
        element = driver.execute_script(
            "return document.getElementById('name');")
        time.sleep(3)
        
        element.send_keys("Test")
        time.sleep(3)
        
        driver.quit()


js = javaScriptExecute()
js.test()
