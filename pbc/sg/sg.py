from abc import ABCMeta, abstractmethod
import time

class BaseGrid:
    __metaclass__ = ABCMeta

    @abstractmethod
    def start_hub(self):
        pass

    @abstractmethod
    def download(self):
        pass

    @abstractmethod
    def add_node(self):
        pass


class Grid(BaseGrid):
    def __init__(self, ssh_client):
        self._client = ssh_client

    def download(self):
        print 'Download'
        self._client.execute('[ -f selenium-server-standalone-3.8.0.jar ] && "Selenium package already exists" || wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X ')
        time.sleep(10)
        # simple loop
        # count = 0
        # while count < 100:
            # if loaded:
            #   return
            # time.sleep(0,5)
            # count +=1
        # raise Exception('File was not loaded')

    def start_hub(self):
        print 'Start hub'
        time.sleep(7)
        self._client.execute('java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &')

    def add_node(self):
        print 'Add node'
        time.sleep(7)
        self._client.execute(
            'java -jar selenium-server-standalone-3.8.0.jar -role node  -hub http://localhost:4444/grid/register >> log.txt 2>&1 &')


def is_installed():
    return True

class StartGrid(BaseGrid):
    def __init__(self, grid):
        self._g = grid

    def download(self):
        # if not is_installed():
            self._g.download()

    def start_hub(self):
        self._g.start_hub()

    def add_node(self):
        self._g.add_node()