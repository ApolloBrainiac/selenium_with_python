from selenium import webdriver
import time


class RadioButtons():

    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        bmwRadioBtn = driver.find_element_by_id('bmwradio')
        bmwRadioBtn.click()

        time.sleep(2)
        benzRadioBtn = driver.find_element_by_id('benzradio')
        benzRadioBtn.click()

        time.sleep(2)
        bmwCheckBox = driver.find_element_by_id('bmwcheck')
        bmwCheckBox.click()

        time.sleep(2)
        benzCheckBox = driver.find_element_by_id('benzcheck')
        benzCheckBox.click()


rb = RadioButtons()
rb.test()
