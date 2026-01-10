from playwright.sync_api import Page


def test_NetworkOne(page: Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role('button', name= "Login").click()
    page.get_by_role('button', name= "ORDERS").click()