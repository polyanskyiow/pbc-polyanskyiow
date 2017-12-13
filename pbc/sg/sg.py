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

    def is_selenium_downloaded(self):
        return self._client.execute('[ -f selenium-server-standalone-3.8.0.jar ] && echo \'True\'')

    def is_conf_file_downloaded(self):
        return self._client.execute('[ -f sg-node.json ] && echo \'True\'')

    def is_hub_running(self):
        result = False
        counter = 0
        while(True):
            print 'Checking if the hub is running'
            if '200' in self._client.execute('curl -o -I -s -w "%{http_code}\\n" http://localhost:4444/hub'):
                result = True
                break
            else:
                time.sleep(1)
            if(counter > 7):
                break
            counter += 1
        return result

    def is_node_running(self):
        result = False
        counter = 0
        while(True):
            print 'Checking if the node is running'
            if '200' in self._client.execute('curl -o -I -s -w "%{http_code}\\n" http://localhost:5555/hub/sessions'):
                result = True
                break
            else:
                time.sleep(1)
            if(counter > 7):
                break
            counter += 1
        return result

    def download(self):
        if(self.is_selenium_downloaded()):
            print 'Selenium has been already downloaded'
        else:
            print 'Starting selenium downloading '
            self._client.execute('wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X ')
            counter = 0
            while ( self._client.execute('pgrep wget | wc -l') == 1): #check if wget process finished
                time.sleep(1)
                if (counter > 15):
                    raise Exception('File has not been fully loaded')
                    break
                counter += 1

        if (self.is_conf_file_downloaded()):
            print 'Configuration file has been already downloaded'
        else:
            print 'Starting configuration file downloading '
            self._client.execute('wget -O sg-node.json https://gist.github.com/extsoft/aed4cb6e0b1ae3cd1d38cafffdd79310/raw/ ')
            counter = 0
            while (self._client.execute('pgrep wget | wc -l') == 1):  # check if wget process finished
                time.sleep(1)
                if (counter > 15):
                    raise Exception('File has not been fully loaded')
                    break
                counter += 1

    def start_hub(self):
        if(self.is_hub_running()):
            print 'Selenium hub is already running'
        else:
            print 'Starting selenium hub '
            self._client.execute('java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &')
            counter = 0
            while (not self.is_hub_running()):
                time.sleep(1)
                if (counter > 7):
                    raise Exception('Selenium hub has not been started')
                    break
                counter += 1

    def add_node(self):
        if (self.is_node_running()):
            print 'Selenium node is already running'
        else:
            print 'Adding selenium node '
            self._client.execute('java -jar selenium-server-standalone-3.8.0.jar -role node -nodeConfig sg-node.json >> log.txt 2>&1 &')
            counter = 0
            while (not self.is_node_running()):
                time.sleep(1)
                if (counter > 7):
                    raise Exception('Selenium node has not been added')
                    break
                counter += 1


class StartGrid(BaseGrid):
    def __init__(self, grid):
        self._g = grid

    def download(self):
        self._g.download()

    def start_hub(self):
        self._g.start_hub()

    def add_node(self):
        self._g.add_node()