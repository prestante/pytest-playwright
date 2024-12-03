"""
This is a test module example from playwright.dev with a standalone code for debugging
"""

import re
from time import sleep
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("playwright", re.IGNORECASE))

    sleep(1)


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

    sleep(1)


if __name__ == "__main__":
    from time import sleep
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Visible browser for debugging
        page = browser.new_page()
        page.goto("https://playwright.dev/")
        print(page.title())  # Debug output
        sleep(1)
        browser.close()