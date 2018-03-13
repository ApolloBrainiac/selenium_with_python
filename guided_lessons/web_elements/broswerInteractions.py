from selenium import webdriver

class BroswerInteractions():

	def test(self):
		baseUrl= 'https://letskodeit.teachable.com/p/practice'
		driver = webdriver.Firefox()

		# Window Maximize

		# Open the Url

		# Get Title

		print("Title of the web page is: ")

		# Get Current Url

		print("Current Url of the web page is: ")

		# Broswer Refresh

		print("Browser Refreshed 1st time")

		print("Browser Refreshed 2nd time")

		# Open another Url

		# Browser Back		



bi = BroswerInteractions()
bi.test