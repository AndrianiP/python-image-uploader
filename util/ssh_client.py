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
        
        
    def uploadFiles(self, filePaths) -> List[str]:
        print("ATTEMPTING TO UPLOAD")
        sftpClient = self.client.open_sftp()
        try:
            for path in filePaths:
                remotePath = pathlib.PurePath(path).name
                print(f"REMOTE PATH: {remotePath}")
                sftpClient.put(path,remotePath)
        finally:
            stdout=self.client.exec_command("ls")
            filePaths = []
            for output in stdout:
                path = str(output)
                if path.endswith(".png") or path.endswith(".jpg"):
                    filePaths.append(path)
            sftpClient.close()
            print("SFTP CLOSED")
            return filePaths
        
    def downloadFiles(self, downloadPath):
        sftpClient = self.client.open_sftp()
        sftpClient.get(downloadPath, os.getenv("DOWNLOAD_PATH") + downloadPath)
        sftpClient.close()
        

# test = Client()
# test.uploadFiles(["D:/Pictures/Camera Roll/3_green.png"])
# test.downloadFiles("TF141 Site Color.png")

# uploader=test.client.open_sftp()
# uploader.put("D:/Pictures/Camera Roll/4_pink.png","4_pink.png")
# stdin,stdout,stderr=test.client.exec_command("ls")
# uploader.close()
# print(stdout.readlines())
# # → [u’Desktop\n’,u’Documents\n’,u’Downloads\n’,u’Videos\n’]
# print(stderr.readlines())
# # → []