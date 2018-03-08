from selenium import webdriver


class FindByXpathCss():

    def test(self):
        driver = webdriver.Firefox()
        driver.get('https://letskodeit.teachable.com/p/practice')

        elementByXpath = driver.find_element_by_xpath("//cd input[@id='name']")

        elementByCss = driver.find_element_by_css_selector("#displayed-text")

        if elementByXpath is not None:
            print("We found an element by xpath")

        if elementByCss is not None:
            print("We found an element by css selector")


fx = FindByXpathCss()
fx.test()
