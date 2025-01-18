import time

from playwright.sync_api import Playwright, expect
from playwright.sync_api import Page
from utils.api_base import Apiutils

# data for "test_mock_empty_orders" test function
fake_payload_response = {"data":[],"message":"No Orders"}
# Intercepting network requests and mocking responses
# API call from browser to server -> API call contact server and return response
# -> browser renders the response
def intercept_response(route):
    route.fulfill(json=fake_payload_response)

def test_mock_empty_orders(page: Page):
    page.goto('https://rahulshettyacademy.com/client')
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)

    # login and go to orders list
    page.locator('#userEmail').fill('test@test.ru')
    page.locator('#userPassword').fill('Resiver28')
    page.locator('#login').click()
    page.get_by_role('button', name='ORDERS').click()
    order_text = page.locator('.mt-4').text_content()
    assert order_text == ' You have No Orders to show at this time. Please Visit Back Us ',\
        "Mocking text isn't matching"
    page.close()




# Intercepting network request with query parameter where order ID "id=6711e249ae2afd4c0b9f6fb0"
# belongs to another user 6701364cae2afd4c0b90113c or 6711e249ae2afd4c0b9f6fb0
def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0")

def test_check_with_different_user_order_id_security(page: Page):
    page.goto('https://rahulshettyacademy.com/client')
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.locator('#userEmail').fill('test@test.ru')
    page.locator('#userPassword').fill('Resiver28')
    page.locator('#login').click()
    page.get_by_role('button', name='ORDERS').click()
    page.get_by_role('button', name='View').first.click()
    unauthorized_message = page.locator('.blink_me').text_content()
    # way 1
    assert unauthorized_message == 'You are not authorize to view this order',\
        "Unauthorized message isn't matching"
    # way 2
    assert page.locator('.blink_me').inner_text() == 'You are not authorize to view this order',\
        "Unauthorized message isn't matching"
    # way 3
    expect(page.locator('.blink_me')).to_have_text('You are not authorize to view this order')

def test_session_storage(playwright: Playwright):
    api_utils =  Apiutils()
    token = api_utils.login_api(playwright)
    assert token is not None, "Token is None"
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context
    page = context.new_page()

    # script to inject token into session storage
    page.add_script_tag(f"""local_storage_set_item('token', + {token} + ')""")
    page.goto('https://rahulshettyacademy.com/client')









