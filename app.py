from playwright.sync_api import sync_playwright
from time import perf_counter #gives us time stamps 

with sync_playwright() as playwright:
    #lauch browser
    browser = playwright.chromium.launch(headless=False, slow_mo= 500) #to see the interface
    #create a new page
    page = browser.new_page()
    print("Page loading...")
    start = perf_counter()

    page.goto(
        "https://bootswatch.com/default",
        wait_until='domcontentloaded', # we can skip the 'load' to obtain just the html
        )

    time_taken = perf_counter() - start
    print(f"...Page loaded in {round(time_taken, 2)}s")
    # 2 decimal places
    browser.close()