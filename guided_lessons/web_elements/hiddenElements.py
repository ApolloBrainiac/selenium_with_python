from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class HiddenElements():
    def testLetsKodeIt(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)

        # Find the state of the text box
        textBoxElement = driver.find_element(By.ID, 'displayed-text')
        print("Text is visible? " +)

        # Click the Hide button

        # Find the state of the text box

        # Click the Show button

        # Find the state of the text box

        # Browser CLose

    def testExpedia(self):
        baseUrl = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)

        flightTab = driver.find_element(By.ID, 'tab-flight-tab-hp')
        flightTab.click()
        
        drpdwnElement = driver.find_element(By.ID, 'flight-age-select-1')


he = HiddenElements()
he.testLetsKodeIt()
