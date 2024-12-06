from playwright.sync_api import Page, expect

def test_add_to_cart(logged_page: Page) -> None:
    lot_title = logged_page.locator('#item_3_title_link > div').text_content()
    lot_price = logged_page.locator("#inventory_container > div > div:nth-child(6) > div.inventory_item_description > div.pricebar > div").text_content()
    print(f"{lot_title} {lot_price}")

    logged_page.locator('[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
    expect(logged_page.locator('[data-test="shopping-cart-badge"]')).to_be_visible(timeout=500)

    # logged_page.wait_for_timeout(1000)  # This is made to pause the test to see the final state of the page
    # logged_page.pause()  # Pause can be used for debugging purposes in headed mode.