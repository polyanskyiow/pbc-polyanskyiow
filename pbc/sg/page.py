class GridPage():

    def __init__(self, driver):
        self._driver =  driver

    def is_title_matches(self):
        return 'Grid Console' in self._driver.get_title()

    def is_node_count_matches(self):
        return 5 == self._driver.elements_count()


