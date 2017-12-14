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

@pytest.fixture(scope="function")
def web_driver():
    driver = WebDriver()
    yield driver
    driver.close()