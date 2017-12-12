from selenium import webdriver

class WebDriver:

    def __init__(self):
        self._driver = webdriver.Firefox()

    def open_page(self, url):
        self._driver.get(url)

    def get_title(self):
        return self._driver.title

    def close(self):
        self._driver.close()

    def elements_count(self):
        return len(self._driver.find_elements_by_xpath("//div[@class='content_detail']//img[contains(@title,'firefox')]"))