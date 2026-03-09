def test_broken_images(browser_context):

    page = browser_context

    page.goto("https://the-internet.herokuapp.com/broken_images")

    images = page.locator("img")

    for i in range(images.count()):

        src = images.nth(i).get_attribute("src")

        response = page.request.get(src)

        assert response.status == 200