from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ExplicitWait():
	def test(self):
		baseUrl = "https://www.expedia.com"
		driver = webdriver.Firefox()
		driver.maximize_window()
		driver.get(baseUrl)
		driver.find_element(By.ID, "tab-flight-tab-hp").click()
		driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
		driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
		driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("12/24/2018")
		returnDate = driver.find_element(By.ID, "flight-returning-hp-flight")
		returnDate.clear()
		returnDate.send_keys("12/26/2018")
		driver.find_element(By.XPATH,
		    "//form[@id='gcw-flights-form-hp-flight']//button[@type='submit']").click()
		driver.find_element(By.ID, "stopFilter_stops-0").click()

		time.sleep(2)
		driver.close()


ew = ExplicitWait()
ew.test()