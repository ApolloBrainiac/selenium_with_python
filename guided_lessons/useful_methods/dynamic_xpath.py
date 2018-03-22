from selenium import webdriver
from selenium.webdriver.common.by import By


class DynamicXpath():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        # Login -> Lecture "How to lick and type on a web element"
        driver.find_element(By.LINK_TEXT, "Login").click()
        email = driver.find_element(By.ID, "user_email")
        email.send_keys("test@email.com")
        password = driver.find_element(By.ID, "user_password")
        password.send_keys("abcabc")
        driver.find_element(By.NAME, "commit").click()

        # Search for courses
        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("JavaScript")

        # Select Course
        _course = "//div[contains(@class, 'course-listing-title') and contains(text(), '{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()


dx = DynamicXpath()
dx.test()
