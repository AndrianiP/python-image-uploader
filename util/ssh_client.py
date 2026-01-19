import os
from typing import List
import paramiko
import pathlib

# S/o to these resources this was the easiest part compared to styling with pyqt
# https://medium.com/featurepreneur/ssh-in-python-using-paramiko-e08fd8a039f7
# https://docs.paramiko.org/en/stable/api/sftp.html
class Client():
    def __init__(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=os.getenv("SSH_HOST", "localhost"),
                            port=int(os.getenv("SSH_PORT",2222)), 
                            username=os.getenv("USER_NAME"),
                            password=os.getenv("USER_PASSWORD"))
        
    
    # Establishes a secure file transfer protocol client
    def uploadFiles(self, filePaths):
        sftpClient = self.client.open_sftp()
        try:
            for path in filePaths:
                # Gets just the name of the file from the path
                remotePath = pathlib.PurePath(path).name
                sftpClient.put(path,remotePath)
        finally:
            stdout=self.client.exec_command("ls")
            filePaths = []
            for output in stdout:
                path = str(output)
                # Filters only images to be added
                if path.endswith(".png") or path.endswith(".jpg"):
                    filePaths.append(path)
            sftpClient.close()
        
        # Downloads files to the download path set in environment variables
    def downloadFiles(self, downloadPath):
        sftpClient = self.client.open_sftp()
        sftpClient.get(downloadPath, os.getenv("DOWNLOAD_PATH") + downloadPath)
        sftpClient.close()
    
    def getServerFiles(self)->List[str]:
        # include stdin, stderr to get rid of readlines being unknown since the command returns a tuple
        stdin,stdout,stderr=self.client.exec_command("ls")
        files = stdout.readlines()
        filePaths = []
        for file in files:
            path = str(file).strip()
            if path.endswith(".png") or path.endswith(".jpg"):
                filePaths.append(path)
        return filePaths
    
    def printServerFiles(self):
        print(self.getServerFiles())
        
