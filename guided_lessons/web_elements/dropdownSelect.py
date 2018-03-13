from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DropDown():
	def test(self):
		baseUrl = 'https://letskodeit.teachable.com/p/practice'
		driver = webdriver.Firefox()
		driver.maximize_window()
		driver.implicitly_wait(10)


dd = DropDown()
dd.test()