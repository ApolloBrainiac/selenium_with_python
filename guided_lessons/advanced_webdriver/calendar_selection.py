from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class calendarSelect():

    def test(self):
        baseUrl = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        # Click flights tab
        driver.find_element(By.ID, "tab-flight-tab-hp")
        # Find departing field
        departingField = driver.find_element(
            By.ID, "flight-departing-hp-flight")
        # Find the date to be selected
        dateToSelect = driver.find_element(By.XPATH, "")
        # Click the date

        time.sleep(3)
        driver.close()


cs = calendarSelect()
cs.test()
