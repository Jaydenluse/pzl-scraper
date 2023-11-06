import sys
import requests

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
        if response.status_code == 200:
            print(f"Successfully uploaded {file_path} to {target_path}")
        else:
            print(f"Failed to upload {file_path}. Status code: {response.status_code} - Response: {response.text}")
            sys.exit(1)  # Exiting with a non-zero status to indicate failure

# Use this function with command-line arguments or adjust as needed