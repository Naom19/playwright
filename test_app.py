#test_app.py

import pytest
from playwright.sync_api import BrowserContext, Page

DOCS_URL = "https://playwright.dev/python/docs/intro"

@pytest.fixture(autouse=True)
def trace_test(context: BrowserContext):
    context.tracing.start(
        name="playwright",
        screenshots=True,
        snapshots=True,
        sources=True,
    )
    yield
    context.tracing.stop(path="trace.zip")

#def test_page_has_get_started_link(browser: Browser):
#    context = browser.new_context(
#        record_video_dir="video/"
#    )
    page = context.new_page()

    page.goto("https://playwright.dev/python")

    theme_btn = page.get_by_title("Switch between dark and light mode (currently dark mode)")
    theme_btn.click()

    link = page.get_by_role("link", name="GET STARTED")
    link.click()
    
    assert page.url == DOCS_URL