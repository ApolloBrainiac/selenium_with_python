from selenium import webdriver

class RunChromeTestsWindows():

	def test(self):
		driver = webdriver.Chrome()

		driver.get("https://letskodeit.teachable.com/")

ct = RunChromeTestsWindows()
ct.test()