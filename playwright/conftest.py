import pytest

@pytest.fixture(scope="session")
def userCredentials(request):
    return request.param


@pytest.fixture(scope="session")
    def browserInstance(playwright):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
