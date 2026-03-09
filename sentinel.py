import argparse
from core.test_runner import SentinelRunner


def main():

    parser = argparse.ArgumentParser(description="SentinelQA Testing Platform")

    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--browser", type=str, default=None)
    parser.add_argument("--network", type=str, default="normal")
    parser.add_argument("--failure", type=str, default="none")
    parser.add_argument("--flaky", type=str, default=None)
    parser.add_argument("--analyze", action="store_true")
    parser.add_argument("--report", action="store_true")

    args = parser.parse_args()

    if args.report:

        from reports.report_generator import ReportGenerator

        generator = ReportGenerator()
        generator.generate()

    elif args.analyze:

        from analytics.qa_analysis import QAAnalysis

        analyzer = QAAnalysis()
        analyzer.analyze()

    # If flaky detection requested
    elif args.flaky:

        from analytics.flaky_detector import FlakyDetector

        detector = FlakyDetector(args.flaky)
        results = detector.run()
        detector.analyze(results)

    else:

        runner = SentinelRunner()

        runner.run_tests(
            workers=args.workers,
            browser=args.browser,
            network=args.network,
            failure=args.failure
        )


if __name__ == "__main__":
    main()