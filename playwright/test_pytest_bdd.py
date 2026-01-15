import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Playwright
from pageObjects.login_page import LoginPage
from utils.apiBaseFramework import APIUtils

# Correct path relative to this file
scenarios("./features/orderTransaction.feature")

# Shared data between steps
@pytest.fixture
def shared_data():
    return {}

# Step Definitions
@given('the user places an order using {username} and {password}')
def place_item_order(playwright: Playwright, username, password, shared_data):
    user_credentials = {"userEmail": username, "userPassword": password}
    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright, user_credentials)
    shared_data["order_id"] = order_id

@given('the user is on the landing page')
def user_on_landing_page(browserInstance, shared_data):
    login_page = LoginPage(browserInstance)
    login_page.navigate()
    shared_data["login_page"] = login_page

@when('the user logs into the portal using {username} and {password}')
def login_to_portal(shared_data, username, password):
    login_page = shared_data["login_page"]
    dashboard = login_page.login(username, password)
    shared_data["dashboard_page"] = dashboard

@when('the user navigates to the orders page')
def navigate_to_orders_page(shared_data):
    dashboard = shared_data["dashboard_page"]
    order_history = dashboard.select_orders_nav_link()
    shared_data["order_history_page"] = order_history

@when('the user selects the order ID')
def select_order_id(shared_data):
    order_history = shared_data["order_history_page"]
    order_id = shared_data.get("order_id")
    details_page = order_history.select_order(order_id)
    shared_data["order_details_page"] = details_page

@then('the order success message should be displayed')
def verify_order_message(shared_data):
    details_page = shared_data["order_details_page"]
    details_page.verify_order_message()
