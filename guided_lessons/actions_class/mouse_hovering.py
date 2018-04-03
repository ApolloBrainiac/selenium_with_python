from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class MouseHover():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        driver.execute_script("window.scrollBy(0, 750);")
        time.sleep(3)
        element = driver.find_element(
            By.ID, "mousehover")
        itemToClickLocator = ".//div[@class='mouse-hover-content']//a[text()='Top']"

        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse Hovered on element")
            time.sleep(2)
            topLink = driver.find_element(
                By.XPATH, itemToClickLocator)
            actions.move_to_element(topLink).click().perform()
            print("Item Clicked")

        except:
            print("Mouse Hover failed on element")


mh = MouseHover()
mh.test()
