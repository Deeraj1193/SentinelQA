from playwright.sync_api import expect


def test_file_upload(browser_context):

    page = browser_context

    page.goto("https://the-internet.herokuapp.com/upload")

    # upload file
    page.set_input_files("#file-upload", __file__)

    page.click("#file-submit")

    uploaded = page.locator("#uploaded-files")

    expect(uploaded).to_be_visible()