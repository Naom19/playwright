#test_app.py

from playwright.sync_api import Page

DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_page_has_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")

    link = page.get_by_role("link", name="GET STARTED")
    link.click()
    #to take an screenshot
    page.screenshot(path="docs.jpg", full_page=True)

    assert page.url == DOCS_URL