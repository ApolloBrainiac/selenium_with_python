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
        textBoxState = textBoxElement.is_displayed() # True if visible, False if hidden
        # Exception if not present in the DOM
        print("Text is visible? " + str(textBoxState))
        time.sleep(3)

        # Click the Hide button
        hideButton = driver.find_element(By.ID, 'hide-textbox')
        hideButton.click()

        # Find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState))
        time.sleep(3)

        # Click the Show button
        showButton = driver.find_element(By.ID, 'show-textbox')
        showButton.click()

        # Find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState))
        time.sleep(3)

        # Browser CLose
        driver.close()

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
