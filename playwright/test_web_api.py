from playwright.sync_api import Playwright
from playwright.sync_api import Page, expect

from utils.apiBase import APIUtils


def test_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order
    apiUtils = APIUtils()
    apiUtils.createOrder(playwright)


    #Login to the System
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role('button', name= "Login").click()

