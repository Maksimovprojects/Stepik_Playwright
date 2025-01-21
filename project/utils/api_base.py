from playwright.sync_api import Playwright


payload_add_item_to_cart = {"_id":"678891a8e2b5443b1f258c71",
                        "product":{"_id":"678522b5e2b5443b1f218601",
                                   "productName":"qwerty",
                                   "productCategory":"fashion",
                                   "productSubCategory":"shirts",
                                   "productPrice":11500,
                                   "productDescription":"Addias Originals",
                                   "productImage":"https://rahulshettyacademy.com/api/ecom/uploads/productImage_1736778421457.png",
                                   "productRating":"0",
                                   "productTotalOrders":"0",
                                   "productStatus":'true',
                                   "productFor":"women",
                                   "productAddedBy":"admin@gmail.com",
                                   "__v":0}}

payload_create_order = {'orders': [{'country': "Russian Federation", 'productOrderedId': "678522b5e2b5443b1f218601"}]}


class Apiutils:

    def login_api(self, playwright: Playwright, user_credentials):
        api_request_context = playwright.request.new_context(base_url='https://rahulshettyacademy.com/client/auth/login')

        login_response = api_request_context.post('/api/ecom/auth/login',
                                                  data={'userEmail': user_credentials['user_email'],
                                                        'userPassword': user_credentials['user_password']},
                                                  headers={'content-type': 'application/json'})
        login_response_body = login_response.json()
        assert  login_response.ok, "Response is not ok"
        token = login_response_body['token']
        print(f"This token from 'login_api' method: {token}")
        return token



    def add_item_to_cart(self, playwright: Playwright, user_credentials):
        token = self.login_api(playwright, user_credentials)
        api_request_context = playwright.request.new_context(base_url='https://rahulshettyacademy.com')
        response = api_request_context.post('api/ecom/user/add-to-cart',
                                 data=payload_add_item_to_cart,
                                 headers={'Authorization': token, 'content-type': 'application/json'}, )
        response.json()
        print(response.json())
        assert response.ok, "Response is not ok"
        print(f"This token from 'add_item_to_cart' method: {token}")



    def create_order(self, playwright: Playwright, user_credentials):
        token = self.login_api(playwright, user_credentials)
        api_request_context = playwright.request.new_context(base_url='https://rahulshettyacademy.com')
        response = api_request_context.post('/api/ecom/order/create-order',
                                 data=payload_create_order,
                                 headers={'Authorization': token, 'content-type': 'application/json'}, )

        create_order_response = response.json()
        order_id = create_order_response['orders'][0]
        assert response.ok, "Response is not ok"
        print(f"This token from 'create_order' method: {token}")
        print(order_id)
        return order_id


