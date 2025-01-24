import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope='session')
def user_credentials(request):
    return request.param

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chromium", help="browser selection")
        # help="browser_name: chromium, firefox, webkit"
    parser.addoption(
        "--url_name_", action="store", default="https://rahulshettyacademy.com/client", help="environment url selection")


@pytest.fixture
def browser_instance(playwright, request):
    browser_name = request.config.getoption("browser_name")
    # url_name = request.config.getoption("url_name_")
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=True)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=True)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    # page.goto(url_name)
    # Start tracing
    # context.tracing.start(screenshots=True, snapshots=True)

    yield page

    # stop tracing and save trace.zip
    # context.tracing.stop(path ="../trace.zip")
    context.close()
    browser.close()

