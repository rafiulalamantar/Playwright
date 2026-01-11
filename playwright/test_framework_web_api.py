import json

import pytest
from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils

with open('playwright/data/credential.json') as f:
    test_data = json.load(f)
    print(test_data)
    userCredentials_list = test_data['user_credentials']


@pytest.mark.parametrize('user_credentials', userCredentials_list)
def test_web_api(playwright: Playwright, user_credentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

#create order
    apiUtils = APIUtils()
    orderId= apiUtils.createOrder(playwright)


    #Login to the System
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill(user_credentials["userEmail"])
    page.get_by_placeholder("enter your passsword").fill(user_credentials["userPassword"])
    page.get_by_role('button', name= "Login").click()
    page.get_by_role('button', name= "ORDERS").click()

    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name= "View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()



