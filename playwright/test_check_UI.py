from time import sleep

from playwright.sync_api import Page, expect

def test_check_iphoneX(page: Page):
    # Verify 2 items are showing in cart
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")  #
    page.get_by_label("Password").fill("learning")  #
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox").check()
    page.get_by_role("button", name="Sign In").click()

    # Find iphone x in items and check presence of item on page
    iphone_x = page.locator("app-card").filter(has_text="iphone X")
    expect(iphone_x).to_be_visible()
    iphone_x.get_by_role("button").click()

    # Find Nokia Edge in items and check presence of item on page
    nokia_edge = page.locator("app-card").filter(has_text="Nokia Edge")
    expect(nokia_edge).to_be_visible()
    nokia_edge.get_by_role("button").click()

    # Verify 2 items are showing in cart
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)









