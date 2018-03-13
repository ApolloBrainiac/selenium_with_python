from selenium import webdriver

class ElementLists():
	def test(self):
		baseUrl = 'https://letskodeit.teachable.com/p/practice'
		driver = webdriver.Firefox()
		driver.maximize_window()
		driver.get(baseUrl)

el = ElementLists()
el.test()