import os
import requests
from dotenv import load_dotenv
load_dotenv()

headers = {"Authorization": f"Bearer {os.getenv('TOKEN')}"}

for i in range(0, 1000):
    response = requests.get(
        "https://2f0037b0-c41b-4087-a625-73f6bebe7d10.app.gra.ai.cloud.ovh.net/", headers=headers)
    assert response.status_code == 200
