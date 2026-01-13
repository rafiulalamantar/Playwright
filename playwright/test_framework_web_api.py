import json

import pytest
from playwright.sync_api import Playwright

from pageObjects.login_page import LoginPage
from utils.apiBaseFramework import APIUtils

#pytest --browser_name chrome -n 3 --tracing on --html=report.html

with open('data/credential.json') as f:
    test_data = json.load(f)
    print(test_data)
    userCredentials_list = test_data['user_credentials']

@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials', userCredentials_list)
def test_web_api(playwright: Playwright, browserInstance,user_credentials):
    user_email = user_credentials["userEmail"]
    password = user_credentials["userPassword"]

    # Launch browser

    # Create order via API
    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright, user_credentials)

    # Login and navigate
    login_page = LoginPage(browserInstance)
    login_page.navigate()
    dashboard = login_page.login(user_email, password)
    order_history_page = dashboard.select_orders_nav_link()
    order_details_page = order_history_page.select_order(order_id)

    # Verify order
    order_details_page.verify_order_message()



