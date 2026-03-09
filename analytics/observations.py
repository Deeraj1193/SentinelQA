class ObservationEngine:

    def generate(self, total, passed, failed, durations):

        observations = []

        # Test outcome
        if failed == 0:
            observations.append("All tests passed successfully.")
        else:
            observations.append(f"{failed} test(s) failed during execution.")

        # Browser performance
        browser_times = {}

        for test, duration in durations:

            if "[" in test and "]" in test:
                browser = test.split("[")[1].replace("]", "")

                if browser not in browser_times:
                    browser_times[browser] = []

                browser_times[browser].append(duration)

        averages = {}

        for browser in browser_times:
            averages[browser] = sum(browser_times[browser]) / len(browser_times[browser])

        if averages:

            fastest = min(averages, key=averages.get)
            slowest = max(averages, key=averages.get)

            observations.append(
                f"{fastest.capitalize()} executed tests fastest ({averages[fastest]:.2f}s avg)."
            )

            observations.append(
                f"{slowest.capitalize()} had the slowest execution time ({averages[slowest]:.2f}s avg)."
            )

        return observations