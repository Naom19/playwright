from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    #lauch browser
    browser = playwright.chromium.launch(headless=False, slow_mo= 500) #to see the interface
    #create a new page
    page = browser.new_page()
    #visit playwright website
    page.goto("https://bootswatch.com/default")

    link = page.locator("a.dropdown-item").first.click()
    link.click(force = True)

    browser.close()