from selenium import webdriver


class ElementState():
    def isEnable(self):
        baseUrl = 'https://www.google.com'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)