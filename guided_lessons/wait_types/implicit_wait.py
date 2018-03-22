from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ImplicitWait():
    test(self):
    baseUrl = "https://letskodeit.teachable.com"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(baseUrl)

    loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
    loginLink.click()

    emailField = driver.find_element(By.ID, "user_email")
    emailField.send_keys("test")


iw = ImplicitWait()
iw.test()