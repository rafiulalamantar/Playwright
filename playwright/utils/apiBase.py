from playwright.sync_api import Playwright

ordersPayload = {{"orders":[{"country":"British Indian Ocean Territory","productOrderedId":"6960eac0c941646b7a8b3e68"}]}}
class APIUtils:

    def createOrder(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order", data=ordersPayload, headers = {"Authorization" : token, "Content-Type" : "application/json"})
        print(response.json())
