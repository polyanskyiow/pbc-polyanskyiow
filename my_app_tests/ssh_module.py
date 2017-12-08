import paramiko
import base64
import time

def run_command(command_to_run):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect('192.168.33.10', username='vagrant', password='vagrant')
    # command_to_run = ["java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &;",
    #                   "java -jar selenium-server-standalone-3.8.0.jar -role node  -hub http://localhost:4444/grid/register >> log.txt 2>&1 &",
    #                   "pgrep java",
    #                   ]
    # j=0;
    # for i in command_to_run:
    #     stdin, stdout, stderr = client.exec_command(command_to_run[j])
    #     for line in stdout:
    #             print(line.strip('\n'))
    #     j+=1
    stdin, stdout, stderr = client.exec_command(command_to_run)
    client.close()

run_command("java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &;")
time.sleep(7) #dirty hack for wait
run_command("java -jar selenium-server-standalone-3.8.0.jar -role node  -hub http://localhost:4444/grid/register >> log.txt 2>&1 &")
# run_command("pgrep java")