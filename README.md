# python-image-uploader
Image Uploader and Downloader built with PyQt while listening to "Bon Iver, Bon Iver" by Bon Iver, and a lot of other things. This took longer than i expected cause of how structuring and styling pyqt is, and i never used it before.


# Guide

## Fill out your Local Environment Variables
Either copy the contents of .env.example and paste the them into .env or put your own values

```
SSH_PORT="2222"
USER_NAME="thank"
USER_PASSWORD="yall"
PASSWORD_ACCESS="true"
DOWNLOAD_PATH="./images/"
```

## Start a docker container

In your terminal run `docker compose up` after your .env file has been populated.

## Run App.py

Run App.py then drag and drop files into the "Drag Drop" area. If you are happy with the files selected, click **Upload**. If you want to reset the list of files to be uploaded, click **Cancel**.

## How to get into SSH to check if files been uploaded
Run `ssh -p <port> <userName>@<host>`. If you are running it locally the host will be `localhost`.

