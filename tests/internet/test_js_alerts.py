from playwright.sync_api import expect


def test_js_alerts(browser_context):

    page = browser_context

    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    # handle alert dialog
    page.once("dialog", lambda dialog: dialog.accept())

    page.click("text=Click for JS Alert")

    result = page.locator("#result")

    expect(result).to_have_text("You successfully clicked an alert")