from selenium import webdriver


class FindByClass():
    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementByClassName = driver.find_element_by_class_name(
            'displayed-class')
        elementByClassName.send_keys("Test the element")

        if elementByClassName is not None:
            print('Found an element by its class.')

        elementByTagName = driver.find_element_by_tag_name('h1')
        text = elementByTagName.text

        if elementByTagName is not None:
            print('Element text is: ' + text)


fbc = FindByClass()
fbc.test()
