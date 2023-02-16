import os
import threading
import speech_to_text as module
from playwright.sync_api import Playwright, sync_playwright
from dotenv import load_dotenv
load_dotenv()


headers = {"Authorization": f"Bearer {os.getenv('TOKEN')}"}


def worker(thread_id):
    while True:
        with sync_playwright() as playwright:
            module.run(playwright)
        print("done")


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
