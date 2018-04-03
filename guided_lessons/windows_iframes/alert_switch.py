from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class AlertSwitch():

    def test(self):
        baseUrl = "https://letskodit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        element = driver.find_element(
            By.ID, "name")
        element.send_keys("Andrew")
        time.sleep(4)

        alertBtn = driver.find_element(
            By.ID, "alertbtn")
        alertBtn.click()
        time.sleep(4)

        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(3)

        element.send_keys("Andrew")
        confirmBtn = driver.find_element(
            By.ID, "confirmbtn")
        confirmBtn.click()
        time.sleep(3)

        alert2 = driver.switch_to.alert
        alert2.dismiss()


al = AlertSwitch()
al.test()
