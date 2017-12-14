from abc import ABCMeta, abstractmethod

class Page():
    __metaclass__ = ABCMeta

    @abstractmethod
    def open(self):
        pass


class GridPage(Page):
    def __init__(self, driver):
        self._driver = driver

    def open(self):
        self._driver.open_page('http://192.168.33.10:4444/grid/console')

    def is_title_matches(self):
        return 'Grid Console' in self._driver.get_title()

    def is_node_count_matches(self):
        return 5 == self._driver.elements_count()

class PythonPage(Page):
    def __init__(self, driver):
        self._driver = driver

    def open(self):
        self._driver.open_page('http://www.python.org')

    def is_title_matches(self):
        return 'Python' in self._driver.get_title()

    def screenshot(self, name):
        self._driver.screenshot(name)

    def search_for(self, search_str):
        self._driver.search_for(search_str)

