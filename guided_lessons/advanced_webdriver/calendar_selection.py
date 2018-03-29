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
        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        # Find departing field
        departingField = driver.find_element(
            By.ID, "flight-departing-hp-flight")
        # Click to departing field
        departingField.click()
        # Find the date to be selected
        dateToSelect = driver.find_element(
            By.XPATH, "//div[@class='datepicker-cal-month'][position()=1]//button[text()='31']")
        # Click the date
        dateToSelect.click()

        time.sleep(3)
        driver.close()

    def test2(self):
        baseUrl = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        # Click flights tab
        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        # Click departing field
        driver.find_element(By.ID, "flight-departing-hp-flight").click()
        calMonth = driver.find_element(
            By.XPATH, "//div[@class='datepicker-cal-month'][position()=1]")
        allValidDates = calMonth.find_elements(
            By.XPATH, "//button[not(contains(@class, 'disabled'))]")

        time.sleep(2)

        for date in allValidDates:
            if date.text == "31":
                date.click()
                break

        driver.quit()


cs = calendarSelect()
cs.test2()
