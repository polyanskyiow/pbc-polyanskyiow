import paramiko
import time

import pytest

from pbc.sg.connections import SshClient

@pytest.fixture(scope="session")
def ssh_client():
    connection = SshClient('192.168.33.10', 'vagrant', 'vagrant') # use paramiko
    yield connection
    connection.close()