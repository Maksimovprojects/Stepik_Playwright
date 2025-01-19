import json
from playwright.sync_api import Playwright, expect
from project.utils.api_base import Apiutils


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()

    # json file with credentials
    with open('../data/credentials.json') as file:
        test_data = json.load(file)
        print(test_data)

    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True)
    page = context.new_page()

    # login and validate added item and placed order
    page.goto('https://rahulshettyacademy.com/client')
    page.locator('#userEmail').fill('test_project@test_project.ru')
    page.locator('#userPassword').fill('Resiver28')
    page.locator('#login').click()

    # add item to cart
    apiutils = Apiutils()
    apiutils.add_item_to_cart(playwright)

    # create order
    apiutils.create_order(playwright)
    order_id = apiutils.create_order(playwright)

    #go to orders history page, check UI order name matches with order name created by API
    page.get_by_role('button', name='ORDERS').click()
    expect(page.locator('tbody .ng-star-inserted').filter(has_text=order_id)).not_to_be_empty()

    # Getting the row with the orders and filtering the button "view" into our order id row, narrowing the search
    row = page.locator('tr').filter(has_text=order_id)
    row.get_by_role('button', name='View').click()
    expect(page.locator('.tagline')).to_contain_text('Thank you for Shopping With Us')

    # stop tracing
    context.tracing.stop(path ="../trace.zip")
    context.close()

