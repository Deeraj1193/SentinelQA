from PIL import Image, ImageChops
import os


class VisualRegression:

    def __init__(self):
        self.base_dir = "visual"
        self.baseline_dir = os.path.join(self.base_dir, "baselines")
        self.compare_dir = os.path.join(self.base_dir, "comparisons")
        self.diff_dir = os.path.join(self.base_dir, "diffs")

        os.makedirs(self.baseline_dir, exist_ok=True)
        os.makedirs(self.compare_dir, exist_ok=True)
        os.makedirs(self.diff_dir, exist_ok=True)

    def compare(self, test_name, browser_name, screenshot_path):

        baseline_path = os.path.join(self.baseline_dir, f"{test_name}_{browser_name}.png")
        current_path = os.path.join(self.compare_dir, f"{test_name}_{browser_name}.png")

        # Create baseline if it doesn't exist
        if not os.path.exists(baseline_path):
            os.rename(screenshot_path, baseline_path)
            print(f"Baseline created for {test_name} ({browser_name})")
            return True

        os.replace(screenshot_path, current_path)

        baseline = Image.open(baseline_path).convert("RGB")
        current = Image.open(current_path).convert("RGB")

        diff = ImageChops.difference(baseline, current)

        if diff.getbbox() is None:
            return True

        diff_path = os.path.join(self.diff_dir, f"{test_name}_{browser_name}_diff.png")
        diff.save(diff_path)

        print(f"Visual regression detected: {test_name} ({browser_name})")

        return False