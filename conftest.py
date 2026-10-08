import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            slow_mo=500
        )

        context = browser.new_context()

        context.tracing.start(
            screenshots=True
        )

        page = context.new_page()
        page.set_default_timeout(60000)

        yield page

        context.tracing.stop(path="trace.zip")
        browser.close()