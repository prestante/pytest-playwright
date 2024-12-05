import pytest
from time import sleep
from playwright.sync_api import Page, expect

@pytest.fixture()
def logged_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
    return page

def test_add_to_cart(logged_page: Page) -> None:
    lot_title = logged_page.locator('#item_3_title_link > div').text_content()
    lot_price = logged_page.locator("#inventory_container > div > div:nth-child(6) > div.inventory_item_description > div.pricebar > div").text_content()
    print(f"{lot_title} {lot_price}")

    logged_page.locator('[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
    expect(logged_page.locator('[data-test="shopping-cart-badge"]')).to_be_visible()

    

    # sleep(1)