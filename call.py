from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(
        "https://2f0037b0-c41b-4087-a625-73f6bebe7d10.app.gra.ai.cloud.ovh.net/")
    # ---------------------
    context.close()
    browser.close()


for i in range(0, 1000):
    with sync_playwright() as playwright:
        run(playwright)
