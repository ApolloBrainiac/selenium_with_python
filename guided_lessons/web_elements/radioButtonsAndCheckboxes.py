from selenium import webdriver

class RadioButtons():

	def test(self):
		baseUrl = 'https://letskodeit.teachable.com'
		driver = webdriver.Firefox()
		driver.maximize_window()
		driver.get(baseUrl)
		driver.implicitly_wait(10)


rb = RadioButtons()
rb.test()