"""
This is a test module example from playwright.dev
"""

import re
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(autouse=True)
def before_each_after_each(page: Page):
    # Go to the starting url before each test for this module (each function of the module will have its own fresh page object with playwright.dev).
    page.goto("https://playwright.dev/")
    
def test_main_navigation(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_url("https://playwright.dev/", timeout=100)

def test_has_title(page: Page):
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("playwright", re.IGNORECASE), timeout=100)