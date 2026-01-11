class LoginPage:
    def __init__(self,page):
        self.page = page


    def navigate(self, page):
        page.goto("https://rahulshettyacademy.com/client/")