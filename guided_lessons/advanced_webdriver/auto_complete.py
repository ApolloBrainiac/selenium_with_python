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

        # Send Partial Data
        cityField = driver.find_element(
            By.ID, "air-city-departure")
        cityField.send_keys("New York")
        time.sleep(3)
        # Find the item and click
        itemToSelect = driver.find_element(
            By.XPATH, "//li[@id='air-city-departure-menu-item2']")
        itemToSelect.click()

        time.sleep(3)
        driver.quit()


ac = autoComplete()
ac.test()
