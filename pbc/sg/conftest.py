import pytest

from pbc.sg.connections import SshClient
from pbc.sg.webdriver import WebDriver

@pytest.fixture(scope="session")
def ssh_client():
    connection = SshClient('192.168.33.10', 'vagrant', 'vagrant')
    yield connection
    #clean up after the tests
    connection.execute('killall java')
    connection.execute('rm -r selenium*')
    connection.execute('rm -r log*')
    connection.execute('rm -r sg-node*')

    connection.close()

@pytest.fixture(scope="module")
def web_driver():
    driver = WebDriver()
    driver.open_page('http://192.168.33.10:4444/grid/console')
    yield driver
    driver.close()
