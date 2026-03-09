import json
import os
from datetime import datetime

METRICS_FILE = "analytics/metrics.json"


class MetricsStore:

    def __init__(self):
        if not os.path.exists(METRICS_FILE):
            self._init_metrics()

    def _init_metrics(self):
        data = {
            "total_tests": 0,
            "failures": 0,
            "screenshots": 0,
            "browsers": {},
            "last_run": None
        }

        with open(METRICS_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        with open(METRICS_FILE) as f:
            return json.load(f)

    def save(self, data):
        with open(METRICS_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def record_test(self, browser, passed):
        data = self.load()

        data["total_tests"] += 1

        if not passed:
            data["failures"] += 1

        if browser not in data["browsers"]:
            data["browsers"][browser] = 0

        data["browsers"][browser] += 1

        data["last_run"] = datetime.now().isoformat()

        self.save(data)

    def record_screenshot(self):
        data = self.load()
        data["screenshots"] += 1
        self.save(data)