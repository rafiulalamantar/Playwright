import pytest
from playwright.sync_api import Page, expect



def test_UIValidationDynamicScript(page: Page):
    # iPhone X, Nokia Edge -> Verify 2 items are showing in Cart
    page.goto("https://rahulshettyacademy.com/client/")

    page.get_by_label("Username:").fill("rahul")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()

    iphone_product = page.locator("app-card").filter(has_text="iPhone X")
    iphone_product.get_by_role("button").click()

    nokia_product = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_product.get_by_role("button").click()

    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

def test_childWindowPage(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newPage_info:
        page.locator(".blinkingText").click()
        childPage = newPage_info.value
        text = childPage.locator(".red").text_content()
        print(text)
        words = text.split("at")
        email = words[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"
