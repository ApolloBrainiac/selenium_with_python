from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class DragDrop():

    def test(self):
        baseUrl = "http://jqueryui.com/droppable/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(4)

        driver.switch_to.frame(0)

        fromElement = driver.find_element(
            By.ID, "draggable")
        toElement = driver.find_element(
            By.ID, "droppable")
        time.sleep(2)

        try:
            actions = ActionChains(driver)
            actions.drag_and_drop(fromElement, toElement).perform()
            print("Drag and drop Element Successful")
            time.sleep(2)
        except:
            print("Drag And Drop failed on element")


dd = DragDrop()
dd.test()
