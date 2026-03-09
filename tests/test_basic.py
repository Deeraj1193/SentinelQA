from analytics.visual_regression import VisualRegression


def test_open_example(browser_context, request):

    page = browser_context

    browser_name = request.node.callspec.params["browser_context"]

    page.goto("https://example.com")

    screenshot_path = f"temp_{browser_name}.png"
    page.screenshot(path=screenshot_path)

    visual = VisualRegression()
    result = visual.compare("example_homepage", browser_name, screenshot_path)

    assert result