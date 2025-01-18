import time
from playwright.sync_api import Page, expect

def test_UI_checks(page: Page):
    # Verify hidden element
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # Test we're on correct web page
    assert page.url == "https://rahulshettyacademy.com/AutomationPractice/"
    expect(page.get_by_placeholder('Hide/Show Example')).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder('Hide/Show Example')).to_be_hidden()

# Alert box handling
def test_ui_alert_handling(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.get_by_role("button", name="Confirm").click()
    page.on("dialog", lambda dialog:dialog.accept())

def test_ui_iframe_handling(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    frame_section = page.frame_locator("#courses-iframe")
    frame_section.get_by_role("link", name="All Access plan").click()
    expect(frame_section.locator("body")).to_contain_text("13,522 Happy Subscibers!")

def test_ui_web_table_handling(page: Page):
    # identify price column
    # identify rice row
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    table_columns = page.locator(".table-bordered >> tr th")
    for i in range(table_columns.count()):
        # # approach 1
        # if table_columns.nth(i).text_content() == "Price":
        #     print("Price column found at index: ", i)
        #     break

        # approach 2
        if table_columns.nth(i).filter(has_text="Price").count() > 0:
            price_column_value = i
            print(f"Price column found at index: {price_column_value}")
            break
    rice_row = page.locator("tr").filter(has_text="Rice")

    # get the price of rice
    rice_row.locator("td").nth(price_column_value).text_content()

    print(f"Price of rice is: {rice_row.locator('td').nth(price_column_value).text_content()}")
    # assertion 1
    expect(rice_row.locator("td").nth(price_column_value)).to_have_text('37')
    # assertion 2
    assert rice_row.locator("td").nth(price_column_value).text_content() == "37", "Price of rice ist not 37"

def test_ui_mouse_hover(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()















