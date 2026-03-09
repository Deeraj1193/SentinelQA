from playwright.sync_api import expect


def test_iframe(browser_context):

    page = browser_context

    page.goto("https://the-internet.herokuapp.com/iframe")

    frame = page.frame_locator("#mce_0_ifr")

    editor = frame.locator("#tinymce")

    expect(editor).to_be_visible()

    expect(editor).to_contain_text("Your content goes here.")