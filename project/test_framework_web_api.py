import json
import pytest
from playwright.sync_api import Playwright
from project.pom.login_page import LoginPage
from project.utils.api_base_pom_framework import Apiutils

# json file with credentials
with open('../project/data/credentials.json') as file:
    test_data = json.load(file)
    test_data_list = test_data['user_credentials']
    print(test_data_list)

'''Should we have same name convention 'user_credentials' fixture and 'user_credentials' parametrize?'''
@pytest.mark.smoke
@pytest.mark.parametrize("user_credentials", test_data_list)
def test_e2e_web_api(playwright: Playwright, user_credentials, browser_instance):
    user_name = user_credentials['user_email']
    user_password = user_credentials['user_password']

    apiutils = Apiutils()
    # create order + retrieve order id on API level
    order_id = apiutils.create_order(playwright, user_credentials)
    # add item to cart
    # apiutils.add_item_to_cart(playwright, user_credentials)

    # login and validate added item and placed order
    login_page = LoginPage(browser_instance)
    login_page.navigate()

    #go dashboard and select orders(transforms to dashboard object class by .login method,
    # it avoids object creation like: dash_page = DashboardPage(page))
    dash_page = login_page.login(user_name, user_password)

    # go to orders history page, check UI order name matches with order name created by API
    order_history_page = dash_page.go_to_orders_page()
    order_details_page = order_history_page.select_order(order_id)
    order_details_page.verify_order_message()

