from project.pom.order_details_page import OrderDetailsPage


class OrderHistory:

    def __init__(self, page):
        self.page = page


    def select_order(self, order_id):
        row = self.page.locator('tr').filter(has_text=order_id)
        row.get_by_role('button', name='View').click()
        order_details_page = OrderDetailsPage(self.page)
        return order_details_page


