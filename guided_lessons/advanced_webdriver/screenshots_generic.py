from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class screenShots():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abc")
        driver.find_element(By.NAME, "commit").click()
        self.takeScreenshot(driver)
        
        time.sleep(3)
        driver.quit()

    def takeScreenshot(self, driver):
        """
        Takes screenshot of the curent open web page
        :param driver:
        :return:
        """
        fileName = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "C:\\Users\\ThunderBear\\Pictures\\"
        destinationFile = screenshotDirectory + fileName

        try:
            driver.save_screenshot(destinationFile)
            print(
                "Screenshot saved to directory --> :: " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")


ss = screenShots()
ss.test()
