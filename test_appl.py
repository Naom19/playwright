from playwright.sync_api import Page, expect

def test_page_has_get_started_link(page:Page):
    page.goto("https://playwright.dev/python")
    input = page.get_by_placeholder("Search docs")

    #input is hidden before btn click
    expect(input).to_be_hidden()

    #search btn
    search_btn = page.get_by_role("button", name ="Search")
    search_btn.press("Control+KeyK") #should pop the search menu

    expect(input).to_be_editable()
    expect(input).to_be_empty()

    #type some query 
    query = "assertions"
    input.fill(query)

    #verify input
    expect(input).to_have_value(query)