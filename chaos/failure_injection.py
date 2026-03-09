class FailureInjector:

    def __init__(self, context):
        self.context = context

    def apply(self, mode):

        if mode == "none":
            return

        if mode == "api_500":
            self.context.route("**/api/**", self._mock_500)
            #self.context.route("**/*", self._mock_500)

        if mode == "api_timeout":
            self.context.route("**/api/**", self._mock_timeout)

    def _mock_500(self, route):
        route.fulfill(
            status=500,
            body="Internal Server Error"
        )

    def _mock_timeout(self, route):
        import time
        time.sleep(5)
        route.abort()