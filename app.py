from playwright.sync_api import sync_playwright


def on_request(request):
    print("Page loaded", page)

with sync_playwright() as playwright:
    #lauch browser
    browser = playwright.chromium.launch(headless=False, slow_mo= 500) #to see the interface
    #create a new page
    page = browser.new_page()


    page.on("request", on_request)
    page.goto("https://bootswatch.com/default")

    browser.close()