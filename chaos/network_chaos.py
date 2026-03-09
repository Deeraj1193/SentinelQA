class NetworkChaos:

    def __init__(self, context):
        self.context = context

    def apply(self, mode):

        if mode == "normal":
            return

        if mode == "offline":
            self.context.set_offline(True)

        if mode == "slow":
            # simulate slow network by throttling requests
            self.context.route("**/*", self._slow_response)

    def _slow_response(self, route):
        import time

        time.sleep(2)  # artificial latency
        route.continue_()