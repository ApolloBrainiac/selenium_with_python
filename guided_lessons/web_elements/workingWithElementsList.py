from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ElementLists():
    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        radioButtonsList = driver.find_elements(By.XPATH,
                                                "//input[contains(@type, 'radio') and contains(@name, 'cars')]")
        size = len(radioButtonsList)
        print("Size of the list: " + str(size))

        for radioButton in radioButtonsList:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(2)


el = ElementLists()
el.test()
