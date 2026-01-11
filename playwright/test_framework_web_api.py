import json

from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils


def test_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

#Json file-> util ->access into test
    with open('playwright/data/credential.json') as f:
        test_data = json.load(f)
        print(test_data)

#create order
    apiUtils = APIUtils()
    orderId= apiUtils.createOrder(playwright)


    #Login to the System
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role('button', name= "Login").click()
    page.get_by_role('button', name= "ORDERS").click()

    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name= "View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()



