from selenium import webdriver


class ElementState():
    def isEnabled(self):
        baseUrl = 'https://www.google.com'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        e1 = driver.find_element_by_id('lst-ib')
        e1.send_keys('letskodeit')

es = ElementState()
es.isEnabled()