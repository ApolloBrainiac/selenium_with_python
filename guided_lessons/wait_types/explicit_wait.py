from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ExplicitWait():
	def test(self):
		baseUrl = "https://www.expedia.com"
		driver = webdriver.Firefox()
		driver.maximize_window()
		driver.get(baseUrl)
		driver.find_element(By.ID, "tab-flight-tab").click()
		driver.find_element(By.ID, "flight-origin").send_keys("SFO")
		driver.find_element(By.ID, "flight-destination").send_keys("NYC")
		driver.find_element(By.ID, "flight-departing").send_keys("12/24/2016")
		returnDate = driver.find_element(By.ID, "flight-returning")
		returnDate.clear()
		returnDate.send_keys("12/26/2016")
		driver.find_element(By.ID, "search-button").click()
		driver.find_element(By.ID, "stopFilter_stops-0").click()

		time.sleep(2)
		driver.close()


ew = ExplicitWait()
ew.test()