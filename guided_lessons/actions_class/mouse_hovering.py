from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class MouseHover():

    def test1(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        driver.execute_script("window.scrollBy(0, 700);")
        time.sleep(2)
        itemToClickLocator = ".//div[@class='mouse-hover-content']//a[text()='Top']"
        try:

        	print("Mouse Hovered on element")
        	time.sleep(2)

        	print("Item Clicked")

        except:
        	print("Mouse Hover failed on element")

        element = driver.find_element(
            By.ID, "")
        element.click()
        time.sleep(4)


mh = MouseHover()
mh.test()
