from playwright.sync_api import Playwright
from pytest_bdd import given

from pageObjects.login_page import LoginPage

from conftest import browserInstance
from utils.apiBaseFramework import APIUtils


@given('place the item order with {username} and {password}')
def place_item_order(playwright,username,password):
    user_credentials={}
    user_credentials["userEmail"] = username
    user_credentials["userPassword"] = password
    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright, user_credentials)
@given('the user is on landing page')
def user_is_on_landing_page(browserInstance):
    login_page = LoginPage(browserInstance)
    login_page.navigate()
