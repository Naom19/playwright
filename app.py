from playwright.sync_api import sync_playwright


def on_load(page):
    print("Page loaded", page)

with sync_playwright() as playwright:
    #lauch browser
    browser = playwright.chromium.launch(headless=False, slow_mo= 500) #to see the interface
    #create a new page
    page = browser.new_page()


    page.on("load", on_load)
    page.goto("https://bootswatch.com/default")

    browser.close()