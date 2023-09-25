import requests
import sys

def upload_to_dropbox(file_path, target_path, access_token):
    url = "https://content.dropboxapi.com/2/files/upload"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Dropbox-API-Arg": f'{{"path": "{target_path}","mode": "add","autorename": true,"mute": false}}',
        "Content-Type": "application/octet-stream"
    }

    with open(file_path, 'rb') as f:
        data = f.read()
        response = requests.post(url, headers=headers, data=data)
        print(response.text)

if __name__ == "__main__":
    file_path = sys.argv[1]
    target_path = sys.argv[2]
    access_token = sys.argv[3]
    upload_to_dropbox(file_path, target_path, access_token)