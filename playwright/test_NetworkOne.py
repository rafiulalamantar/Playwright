from playwright.sync_api import Page, Playwright

from utils.apiBase import APIUtils

#Use Case
# Browser → API request
#       → API request reaches server
#       → Server returns response
#       → Browser uses response to generate HTML


fakePayloadResponse = {
    "data": [],
    "message": "No Orders"
}

def intercept_response(route):
    route.fulfill(
        json=fakePayloadResponse
    )

def test_NetworkOne(page: Page):
    page.route(
        "https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",
        intercept_response
    )
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()

    order_text = page.locator(".mt-4").text_content()
    print(order_text)

def test_session_storage(playwright : Playwright):
    api_utils = APIUtils()
    get_token = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #script to inject token in local storage
    page.add_init_script(f"""localStorage.setItem('token', '{get_token}')""")
    page.goto("https://rahulshettyacademy.com/client/")





