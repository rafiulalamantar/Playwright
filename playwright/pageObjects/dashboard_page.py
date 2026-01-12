from .order_history_page import OrderHistoryPage


class DashboardPage:
    def __init__(self, page):
        self.page = page

    def select_orders_nav_link(self):
        self.page.get_by_role('button', name="ORDERS").click()
        return OrderHistoryPage(self.page)
