import requests
import os
import random
import string
import threading
from dotenv import load_dotenv
load_dotenv()

headers = {"Authorization": f"Bearer {os.getenv('TOKEN')}"}


def worker(thread_id):
    while True:
        response = requests.get(
            "https://2f0037b0-c41b-4087-a625-73f6bebe7d10.app.gra.ai.cloud.ovh.net/", headers=headers)
        print(response.status_code)


threads = []
for i in range(100):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
