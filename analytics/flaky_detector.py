import subprocess


class FlakyDetector:

    def __init__(self, test_path, runs=10):
        self.test_path = test_path
        self.runs = runs

    def run(self):

        results = []

        for i in range(self.runs):

            print(f"Run {i+1}/{self.runs}")

            result = subprocess.run(
                ["pytest", self.test_path, "-q"],
                capture_output=True
            )

            if result.returncode == 0:
                results.append("PASS")
            else:
                results.append("FAIL")

        return results

    def analyze(self, results):

        passes = results.count("PASS")
        fails = results.count("FAIL")

        failure_rate = fails / len(results)

        print("\nRun Results:")
        for r in results:
            print(r)

        print(f"\nFailure Rate: {failure_rate * 100:.1f}%")

        if fails > 0 and passes > 0:
            print("⚠ Test marked as FLAKY")

        elif fails == len(results):
            print("❌ Test consistently failing")

        else:
            print("✅ Test stable")