from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GetAttribute():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        element = driver.find_element(By.ID, 'name')
        elAttr = element.get_attribute("class")

       	print("Value of class is: " + elAttr)
        time.sleep(3)
        driver.quit()


ga = GetAttribute()
ga.test()
