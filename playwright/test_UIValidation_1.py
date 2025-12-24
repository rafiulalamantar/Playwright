from playwright.async_api import Page


def test_UIValidationDynamicScript(page: Page):
    #iPhone X, Nokia Edge -> Verify 2 items are showing in Crat

    page.goto("")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    # page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    iPhoneProcut = page.locator("app-card").filter(has_text="iPhone X")
    iPhoneProcut.locator()