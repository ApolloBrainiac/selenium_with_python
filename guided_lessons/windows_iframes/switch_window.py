from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchWindow():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        # Find parent handle -> Main Window
        parentHandle = driver.current_window_handle
        print("Parent Handle: " + str(parentHandle))

        # Find open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(4)

        # Find all handles, there should be two handles after clicking open window button
        handles = driver.window_handles

        # Switch to window and search course
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to window:: " + handle)
                searchBox = driver.find_element(By.ID, "search-courses")
                searchBox.send_keys("python")
                time.sleep(2)

        # Switch back to the parent handle


sw = SwitchWindow()
sw.test()
