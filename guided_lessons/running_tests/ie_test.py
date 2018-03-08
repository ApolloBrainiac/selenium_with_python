from selenium import webdriver
import os


class RunIETest():

    def test(self):
        driver = webdriver.Ie()
        driver.get('http://www.letskodeit.com')


IeTest = RunIETest()
IeTest.test()
