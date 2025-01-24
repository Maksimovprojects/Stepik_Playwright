import pytest
from pytest_bdd import given, when, then, parsers, scenarios
from test_project.pom.login_page import LoginPage
from test_project.utils.api_base_pom_framework import Apiutils


scenarios('features/order_transaction.feature')

@pytest.fixture
def share_data():
    return {}


@given(parsers.parse('place the item order with {username} and {password}'))
def place_item_order(playwright, username, password, share_data):
    user_credentials = {}
    user_credentials['user_email'] = username
    user_credentials['user_password'] = password
    apiutils = Apiutils()
    # create order + retrieve order id on API level
    order_id = apiutils.create_order(playwright, user_credentials)
    share_data['order_id'] = order_id

@given('the user is on landing page')
def user_is_on_landing_page(browser_instance, share_data):
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    share_data['login_page'] = login_page


@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username, password, share_data):
    login_page = share_data['login_page']
    dash_page = login_page.login(username, password)
    share_data['dash_page'] = dash_page

@when('navigate to orders page')
def navigate_to_orders_page(share_data):
    dash_page = share_data['dash_page']
    order_history_page = dash_page.go_to_orders_page()
    share_data['order_history_page'] = order_history_page

@when('select order id')
def select_order_id(share_data):
    order_history_page = share_data['order_history_page']
    order_id = share_data['order_id']
    order_details_page = order_history_page.select_order(order_id)
    share_data['order_details_page'] = order_details_page


@then('order message is successfully shown in details page')
def verify_order_message(share_data):
    order_details_page = share_data['order_details_page']
    order_details_page.verify_order_message()