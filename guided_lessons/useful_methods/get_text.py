from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GetText():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        openTabElement = driver.find_element(By.ID, 'opentab')
        elText = openTabElement.text
        print("Text on element is: " + elText)
        time.sleep(2)
        driver.quit()


gt = GetText()
gt.test()