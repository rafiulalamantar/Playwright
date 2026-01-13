import pytest

@pytest.fixture(scope="session")
def userCredentials(request):
    return request.param


@pytest.fixture(scope="session")
def browserInstance(playwright,request):
    request.config.getoption("--browser")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
