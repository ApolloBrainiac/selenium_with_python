from selenium import webdriver


class RunFFTests():

    def test(self):
        # Instantiate FF Browser Comman
        driver = webdriver.Firefox()

        # Open the provided URI
        driver.get("https://letskodeit.teachable.com/")


ff = RunFFTests()
ff.test()
