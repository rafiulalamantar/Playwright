import json

import pytest
from playwright.sync_api import Playwright, expect

from pageObjects.LoginPage import LoginPage
from utils.apiBase import APIUtils

with open('playwright/data/credential.json') as f:
    test_data = json.load(f)
    print(test_data)
    userCredentials_list = test_data['user_credentials']


@pytest.mark.parametrize('user_credentials', userCredentials_list)

def test_web_api(playwright: Playwright, user_credentials):

    userEmail = user_credentials["userName"]
    password = user_credentials["userPassword"]

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

#create order
    apiUtils = APIUtils()
    orderId= apiUtils.createOrder(playwright, user_credentials)


    #Login to the System
    loginPage = LoginPage(page)
    loginPage.navigate()
    loginPage.login(userEmail, password)
    page.get_by_role('button', name= "ORDERS").click()

    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name= "View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()



