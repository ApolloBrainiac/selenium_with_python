from selenium import webdriver


class BroswerInteractions():

    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()

        # Window Maximize
        driver.maximize_window()

        # Open the Url
        driver.get(baseUrl)

        # Get Title
        title = driver.title
        print("Title of the web page is: " + title)

        # Get Current Url
        url = driver.current_url
        print("Current Url of the web page is: " + url)

        # Broswer Refresh
        driver.refresh()
        print("Browser Refreshed 1st time")
        driver.get(driver.current_url)
        print("Browser Refreshed 2nd time")

        # Open another Url
        driver.get(
            'https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1')
        # Browser Back
        driver.back()
        print('Go one step back in browser history')

        # Browser Forward
        driver.forward()
        print('Go one step forward in broswer history')
        # Get Page Source
        pageSource = driver.page_source
        # Broswer Close / Quit
        driver.close()


bi = BroswerInteractions()
bi.test()
