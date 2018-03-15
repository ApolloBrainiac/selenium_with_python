from selenium import webdriver
from selenium.webdriver.common.by import By
from wrappers_class import Wrappers


class ElementCheck():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        wr = Wrappers(driver)

        elResult = wr.isElementPresent("name", By.ID)
        print(str(elResult))

        elResult2 = wr.elementPresenceCheck("//input[@id='name']", By.XPATH)
        print(str(elResult2))


ec = ElementCheck()
ec.test()
