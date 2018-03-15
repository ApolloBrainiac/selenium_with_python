from selenium import webdriver
from selenium.webdriver.common.by import By
from useful_methods.wrappers_class import Wrappers
import time


class HandyWrapper():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        wr = Wrappers(driver)

        textField = wr.getElement("name")
        textField.send_keys("Test")
        time.sleep(3)

        textField2 = wr.getElement("//input[@id='name']", locatorType="xpath")
        textField2.send_keys("Test2")
        time.sleep(3)
        driver.quit()

hw = HandyWrapper()
hw.test()
