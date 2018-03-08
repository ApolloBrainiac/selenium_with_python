from selenium import webdriver


class FindByText():
    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementByLinkText = driver.find_element_by_link_text("Login")

        if elementByLinkText is not None:
            print("We found an element by Link Text")

        elementByPartialLinkText = driver.find_element_by_partial_link_text(
            "Prac")

        if elementByPartialLinkText is not None:
            print("We found an element by Partial link Text")


ft = FindByText()
ft.test()
