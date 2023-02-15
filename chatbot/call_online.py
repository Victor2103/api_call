from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(
        "https://76b82cd8-601f-4419-b6ff-ce54bb1e00b9.app.gra.ai.cloud.ovh.net/")
    page.wait_for_load_state()
    page.get_by_role("button").click()
    page.get_by_placeholder("Start typing a message...").fill("hello")
    page.get_by_placeholder("Start typing a message...").press("Enter")
    page.wait_for_load_state()
    page.get_by_placeholder(
        "Start typing a message...").fill("can you help me ?")
    page.get_by_placeholder("Start typing a message...").press("Enter")
    page.wait_for_load_state()
    page.get_by_placeholder("Start typing a message...").fill("it is a house")
    page.get_by_placeholder("Start typing a message...").press("Enter")
    page.wait_for_load_state()
    page.get_by_placeholder("Start typing a message...").fill("bike")
    page.get_by_placeholder("Start typing a message...").press("Enter")
    page.wait_for_load_state()
    page.get_by_placeholder("Start typing a message...").fill("site")
    page.get_by_placeholder("Start typing a message...").press("Enter")
    page.wait_for_load_state()
    page.get_by_placeholder("Start typing a message...").fill("on site")
    page.get_by_placeholder("Start typing a message...").press("Enter")
    page.wait_for_load_state()
    page.get_by_placeholder("Start typing a message...").fill("bye")
    page.get_by_placeholder("Start typing a message...").press("Enter")
    page.wait_for_load_state()
    # ---------------------
    context.close()
    browser.close()


"""
for i in range(0, 100):
    with sync_playwright() as playwright:
        run(playwright)
"""
