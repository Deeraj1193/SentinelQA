import os
from datetime import datetime
from analytics.metrics_store import MetricsStore

metrics = MetricsStore()

class ArtifactManager:

    def __init__(self, browser_name="chromium"):
        self.browser_name = browser_name
        self.base_dir = os.path.join("artifacts", browser_name)

        self.screenshot_dir = os.path.join(self.base_dir, "screenshots")
        self.video_dir = os.path.join(self.base_dir, "videos")
        self.trace_dir = os.path.join(self.base_dir, "traces")
        self.log_dir = os.path.join(self.base_dir, "logs")

        self._ensure_directories()

    def _ensure_directories(self):
        os.makedirs(self.screenshot_dir, exist_ok=True)
        os.makedirs(self.video_dir, exist_ok=True)
        os.makedirs(self.trace_dir, exist_ok=True)
        os.makedirs(self.log_dir, exist_ok=True)

    def generate_filename(self, test_name, extension):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{test_name}_{timestamp}.{extension}"
    
    def capture_screenshot(self, page, test_name):

        filename = self.generate_filename(test_name, "png")
        path = os.path.join(self.screenshot_dir, filename)

        page.screenshot(path=path)

        metrics.record_screenshot()

        return path
