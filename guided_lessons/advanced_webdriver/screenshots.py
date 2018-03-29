from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class screenShots():
    def test(self):
        baseUrl = "https://letskodit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_elment(By.ID, "user_email").send_keys("abc@emial.com")
        driver.find_element(By.ID, "user_password").send_keys("abc")
        driver.find_element(By.NAME, "commit").click()

        time.sleep(3)
        driver.quit()


ss = screenShots()
ss.test()
