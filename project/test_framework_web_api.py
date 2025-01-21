import json
import pytest
from playwright.sync_api import Playwright, expect
from project.pom.dashboard_page import DashboardPage
from project.pom.login_page import LoginPage
from project.pom.order_history import OrderHistory
from utils.api_base import Apiutils

# json file with credentials
with open('../project/data/credentials.json') as file:
    test_data = json.load(file)
    test_data_list = test_data['user_credentials']
    print(test_data_list)

# 1 test will fail due having order_id from another user
@pytest.mark.parametrize("user_credentials", test_data_list)
def test_e2e_web_api(playwright: Playwright, user_credentials):
    user_name = user_credentials['user_email']
    user_password = user_credentials['user_password']
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True)

    apiutils = Apiutils()
    # create order + retrieve order id
    order_id = apiutils.create_order(playwright, user_credentials)
    # add item to cart
    # apiutils.add_item_to_cart(playwright, user_credentials)

    # login and validate added item and placed order
    login_page = LoginPage(page)
    login_page.navigate()
    print(page.url)
    login_page.login(user_name, user_password)

    #go dashboard and select orders(transforms to dashboard object class by .login method,
    # it avoids object creation like: dash_page = DashboardPage(page))
    dash_page = login_page.login(user_name, user_password)

    # go to orders history page, check UI order name matches with order name created by API
    order_history_page = dash_page.go_to_orders_page()
    order_details_page = order_history_page.select_order(order_id)
    order_details_page.verify_order_message()

    # stop tracing
    context.tracing.stop(path ="../trace.zip")
    context.close()
