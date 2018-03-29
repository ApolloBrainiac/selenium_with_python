from traceback import print_stack
from useful_methods.wrappers_class import Wrappers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class ExplicitWaitType():

    def __init__(self, driver):
    	self.driver = driver
    	self.wr = Wrappers(driver)


        def waitForElements(self, locator, locatorType="id",
                            timeout=10, pollFrequency=0.5):
            element = None
            try:
            	byType = self.wr.getByType(locatorType)
                print("Waiting for maximum :: " + str(timeout) +
                      " :: seconds for elment to be clickable")
                wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                     ignored_exceptions=[NoSuchElementException,
                                                         ElementNotVisibleException,
                                                         ElementNotSelectableException])
                element = wait.until(EC.element_to_be_clickable((By.ID, ""stopFilter_stops - 0"")))

                print("Element appeared on the web page")
            except:
                print("Element not appeared on the web page")
                print_stack()
            return element
