from selenium import webdriver
import os

class RunIETestsWindows():

    def test(self):
        driverLocation = "C:\\Users\\ThunderBear\\Downloads\\Applications\\selenium_drivers\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = driverLocation
        driver = webdriver.Ie(driverLocation)
        driver.get("http://www.letskodeit.com")

ieTest = RunIETestsWindows()
ieTest.test()