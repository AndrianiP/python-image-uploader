import os
from typing import List
import paramiko
import pathlib

# from dotenv import load_dotenv

# # 1. LOAD THE DOTENV FIRST
# load_dotenv()

class Client():
    def __init__(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=os.getenv("SSH_HOST", "localhost"),
                            port=int(os.getenv("SSH_PORT",2222)), 
                            username=os.getenv("USER_NAME"),
                            password=os.getenv("USER_PASSWORD"))
        
    
    #TODO ADD COMMENTS
    def uploadFiles(self, filePaths):
        sftpClient = self.client.open_sftp()
        try:
            for path in filePaths:
                remotePath = pathlib.PurePath(path).name
                sftpClient.put(path,remotePath)
        finally:
            stdout=self.client.exec_command("ls")
            filePaths = []
            for output in stdout:
                path = str(output)
                if path.endswith(".png") or path.endswith(".jpg"):
                    filePaths.append(path)
            sftpClient.close()
        
    def downloadFiles(self, downloadPath):
        sftpClient = self.client.open_sftp()
        sftpClient.get(downloadPath, os.getenv("DOWNLOAD_PATH") + downloadPath)
        sftpClient.close()
    
    def getServerFiles(self)->List[str]:
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
        
