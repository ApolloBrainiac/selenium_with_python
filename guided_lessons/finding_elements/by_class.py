from selenium import webdriver
from selenium.webdriver.common.by import By

class ByClass():
    baseUrl = "https://letskodeit.teachable.com/p/practice"
    driver = webdriver.Firefox()
    driver.get(baseUrl)

    elementById = driver.find_element(By.ID, "")

    if elementById is not None:
        print('We found an element by id')

    elementByXpath = driver.find_element(By.XPATH, "")

    if elementByXpath is not None:
        print("We found an element by XPATH")

    elementByLinkText = driver.find_element(By.LINK_TEXT, "")

    if elementByLinkText is not None:
        print("We found an element by Link Text")


fbc = ByClass()
fbc.test()
