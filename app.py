from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    #lauch browser
    browser = playwright.chromium.launch(headless=False, slow_mo= 500) #to see the interface
    #create a new page
    page = browser.new_page()
    #visit playwright website
    page.goto("https://playwright.dev/python")
    #locate a link element with "Docs" text
    docs_button = page.get_by_role('link', name="Docs")
    docs_button.click()
    #get url and print it
    print("Docs:", page.url)

    #locator
    docs_button= page.get_by_role('button', name= "Sign Up")
    docs_button.click()

    browser.close()