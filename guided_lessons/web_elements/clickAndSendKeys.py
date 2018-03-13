from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ClickAndSend():
    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        loginLink = driver.find_element(
            By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginLink.click()

        userEmail = driver.find_element(By.ID, "user_email")
        userEmail.send_keys("test")

        userPassword = driver.find_element(By.ID, "user_password")
        userPassword.send_keys("test")

        time.sleep(3)

        userEmail.clear()

        time.sleep(3)

        userEmail.send_keys("test")


cas = ClickAndSend()
cas.test()
