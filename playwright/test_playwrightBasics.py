import time
from pydoc import pager

import pytest
from playwright.async_api import Playwright
from playwright.sync_api import Page, expect


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")


#chromium headless mode, 1 single context
def test_playwrightShortCut(page: Page):
    page.goto("https://rahulshettyacademy.com")

def test_CoreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learningdd")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    # time.sleep(5)

def test_firefoxBrow(playwright: Playwright):
    firefoxBrowser = playwright.firefox
    browser = firefoxBrowser.launch(headless=False)
    page = browser.new_page()
    page.goto("")
    page.get_by_label("Username:").fill("")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()


