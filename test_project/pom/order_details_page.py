from playwright.sync_api import Playwright, expect

class OrderDetailsPage:
    def __init__(self, page):
        self.page = page

    def verify_order_message(self):
        # Getting the row with the orders and filtering the button "view" into our order id row, narrowing the search
        expect(self.page.locator('.tagline')).to_contain_text('Thank you for Shopping With Us')

