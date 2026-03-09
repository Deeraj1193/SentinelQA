from playwright.sync_api import expect


def test_dynamic_loading(browser_context):

    page = browser_context

    page.goto("https://the-internet.herokuapp.com/")

    # open dynamic loading section
    page.click("text=Dynamic Loading")

    # open example 1
    page.click("text=Example 1: Element on page that is hidden")

    # start loading
    page.click("button:has-text('Start')")

    # wait for Hello World text
    hello = page.locator("#finish h4")

    expect(hello).to_have_text("Hello World!")