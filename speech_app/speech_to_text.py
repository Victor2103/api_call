import os
from playwright.sync_api import Playwright, sync_playwright, expect
from dotenv import load_dotenv
load_dotenv()


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://gra.ai.cloud.ovh.net/v1/oauth/login?redirect=https://2f0037b0-c41b-4087-a625-73f6bebe7d10.app.gra.ai.cloud.ovh.net/&error=unauthorized")
    page.get_by_role("link", name="Login with token").click()
    page.get_by_placeholder("Token").click()
    page.get_by_placeholder("Token").fill(os.getenv("TOKEN"))
    page.get_by_role("button", name="Connect").click()
    # page.wait_for_timeout(60000)
    while page.get_by_role("textbox").is_hidden():
        pass
    page.get_by_role("textbox").fill(
        "https://www.youtube.com/watch?v=4WEQtgnBu0I")
    page.get_by_role("textbox").press("Enter")
    # page.wait_for_timeout(60000)
    while page.get_by_role("button", name="Transcribe audio!").is_hidden():
        pass
    page.get_by_role("button", name="Transcribe audio!").click()
    # page.wait_for_timeout(60000)
    while page.get_by_role("button", name="Download as TXT").is_hidden():
        pass
    with page.expect_download() as download_info:
        with page.expect_popup() as page1_info:
            page.get_by_role("button", name="Download as TXT").click()
        page1 = page1_info.value
    download = download_info.value
    page1.close()

    # ---------------------
    context.close()
    browser.close()


"""
with sync_playwright() as playwright:
    run(playwright)
"""
