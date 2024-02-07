import asyncio
import logging
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async

TARGET_URL = 'http://coppeldigital.com/'

async def capture_screenshot(browser_type):
    async with browser_type.launch() as browser:
        page = await browser.new_page()
        await stealth_async(page)
        await page.goto(TARGET_URL)
        await page.screenshot(path=f'example-{browser_type.name}.png')

async def main():
    logging.basicConfig(level=logging.INFO)

    async with async_playwright() as playwright:
        browser_types = [playwright.chromium, playwright.firefox, playwright.webkit]
        await asyncio.gather(*[capture_screenshot(browser_type) for browser_type in browser_types])

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
