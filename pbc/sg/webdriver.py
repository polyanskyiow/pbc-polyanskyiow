from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


class WebDriver:

    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        self._driver = webdriver.Remote(
        command_executor='http://192.168.33.10:4444/wd/hub',
        desired_capabilities={'browserName': 'firefox'},
        options=options
    )

    def open_page(self, url):
        self._driver.get(url)

    def get_title(self):
        return self._driver.title

    def close(self):
        self._driver.close()

    def screenshot(self, name):
        self._driver.save_screenshot(name)

    def search_for(self, search_str):
        elem = self._driver.find_element_by_name('q')
        elem.clear()
        elem.send_keys(search_str)
        elem.send_keys(Keys.ENTER)

    def elements_count(self):
        return len( self._driver.find_elements_by_xpath("//div[@class='content_detail']//img[contains(@src,'firefox')]") )