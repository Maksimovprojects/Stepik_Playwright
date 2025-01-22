from .order_history import OrderHistory


class DashboardPage():

    def __init__(self, page):
        self.page = page

    def go_to_orders_page(self):
        self.page.get_by_role('button', name='ORDERS').click()
        order_history_page = OrderHistory(self.page)
        return order_history_page