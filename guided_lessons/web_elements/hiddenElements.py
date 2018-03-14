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

        def isVisible():
            textBoxElement = driver.find_element(By.ID, 'displayed-text')
            textBoxState = textBoxElement.is_displayed()  # True if visible, False if hidden
            # Exception if not present in the DOM
            print("Text is visible? " + str(textBoxState))
            time.sleep(3)
        
        # Find the state of the text box
        isVisible()

        # Click the Hide button
        hideButton = driver.find_element(By.ID, 'hide-textbox')
        hideButton.click()

        # Find the state of the text box
        isVisible()

        # Click the Show button
        showButton = driver.find_element(By.ID, 'show-textbox')
        showButton.click()

        # Find the state of the text box
        isVisible()

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
        drpdwnState = drpdwnElement.is_displayed()
        print("Element visible? " + str(drpdwnState))


he = HiddenElements()
he.testLetsKodeIt()
he.testExpedia()
