import os
import paramiko
from dotenv import load_dotenv
load_dotenv()


class Client():
    def __init__(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=os.getenv("SSH_HOST", "localhost"), port=os.getenv("SSH_PORT"), username=os.getenv("USER_NAME"), password=os.getenv("USER_PASSWORD"))
        
        
        

test = Client()
stdin,stdout,stderr=test.client.exec_command("ls")
print(stdout.readlines())
# → [u’Desktop\n’,u’Documents\n’,u’Downloads\n’,u’Videos\n’]
print(stderr.readlines())