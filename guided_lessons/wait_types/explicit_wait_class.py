from traceback import print_stack
from useful_methods.wrappers_class import Wrappers


class ExplicitWaitType():

    def __init__(self, driver):

        def waitForElements(self, locator, locatorType="id",
                            timeout=10, pollFrequency=0.5):
            element = None
            try:
                print("Waiting for maximum :: " + str(timeout) +
                      " :: seconds for elment to be clickable")

                print("Element appeared on the web page")
            except:
                print("Element not appeared on the web page")
                print_stack()
            return element
