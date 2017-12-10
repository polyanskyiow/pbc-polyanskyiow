import paramiko
import base64
import time

def start_selenium_grid():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect('192.168.33.10', username='vagrant', password='vagrant')
    client.exec_command('[ -f selenium-server-standalone-3.8.0.jar ] && "Selenium package already exists" || wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X ')
    time.sleep(15) #dirty hack for timeout
    client.exec_command('java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &')
    time.sleep(10) #dirty hack for timeout
    client.exec_command( 'java -jar selenium-server-standalone-3.8.0.jar -role node  -hub http://localhost:4444/grid/register >> log.txt 2>&1 &')
    client.close()

start_selenium_grid()