from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class screenShots():
	def test(self):
		baseUrl = ""
		driver = webdriver.Firefox()
		driver.maximize_window()
		driver.get(baseUrl)
		driver.implicitly_wait(5)

		element = driver.find_elment(
			By.XPATH, "")
		element.click()

		time.sleep(3)

		driver.quit()

ss = screenShots()
ss.test()