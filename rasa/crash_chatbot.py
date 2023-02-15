import requests
import os
import random
import string
import threading
from dotenv import load_dotenv
load_dotenv()

intent = ["Hello", "Hi", "Bye", "Help me",
          "can you help me ?", "WHo are you ?", "Good Morning"]

body = {"text": random.choice(intent),
        "message_id": ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10000))}

headers = {"Authorization": f"Bearer {os.getenv('TOKEN')}"}


def worker(thread_id):
    while True:
        body = {"text": random.choice(intent),
                "message_id": ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10000))}
        response = requests.post(
            "https://baac2c13-2e69-4d0f-ad6b-dd9efd9be513.app.gra.ai.cloud.ovh.net/model/parse?emulation_mode=LUIS", json=body, headers=headers)
        print(response.text)


threads = []
for i in range(100):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
