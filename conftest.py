import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(autouse=True, scope='package')
def log_test():
    print("\nTest is starting")
    yield
    print("\nTest is ending")

@pytest.fixture()
def logged_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
    return page