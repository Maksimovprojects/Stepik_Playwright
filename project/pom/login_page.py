from .dashboard_page import DashboardPage

class LoginPage():

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto('https://rahulshettyacademy.com/client')

    def login(self, user_name, user_password):
        self.page.locator('#userEmail').fill(user_name)
        self.page.locator('#userPassword').fill(user_password)
        self.page.locator('#login').click()

        # Second way
        # self.page.get_by_placeholder('email@example.com').fill(user_name)
        # self.page.get_by_placeholder('enter your passsword').fill(user_password)
        # self.page.locator('#login').click()

        dashboard_page = DashboardPage(self.page)
        return dashboard_page

