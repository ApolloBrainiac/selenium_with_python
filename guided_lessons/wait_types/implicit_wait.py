from selenium import webdriver
from selenium.webdriver.common import by
import time


class ImplicitWait():
    test(self):
    baseUrl = "https://letskodeit.teachable.com"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(baseUrl)


iw = ImplicitWait()
iw.test()