import time
from pyexpat.errors import messages

from playwright.sync_api import Page

#Use Case
# Browser → API request (order details)
#       → You intercept the request
#       → You modify the request URL
#       → Server returns response
#       → Browser renders HTML based on new response

def intercept_request(route):
    route.continue_(
        url= "https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=69628a16c941646b7a8e245"
    )

def test_NetworkOne(page: Page):
    page.route(
        "https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",
        intercept_request
    )
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)