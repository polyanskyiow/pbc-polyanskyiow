import paramiko

class SshClient:

    def __init__(self, ip, user, pasw):
        self._user = user
        self._pasw = pasw
        self._ip = ip
        self._connection = paramiko.SSHClient()
        self._connection.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        print 'Establishing connection to {ip} with credentials {u}@{p}'.format(ip=self._ip, u=self._user, p=self._pasw)
        self._connection.connect(self._ip, username=self._user, password=self._pasw)

    def execute(self, command):
        print '[{u}:{p} -> {c}]'.format(u=self._user, p=self._pasw, c=command)
        self._connection.exec_command(command)

    def close(self):
        print 'Closing [{u}:{p}]'.format(u=self._user, p=self._pasw)
        self._connection.close()