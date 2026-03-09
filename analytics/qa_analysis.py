import sqlite3


class QAAnalysis:

    def __init__(self, db_path="sentinel_metrics.db"):
        self.conn = sqlite3.connect(db_path)

    def analyze(self):

        cursor = self.conn.cursor()

        print("\nSentinelQA Analysis Report")
        print("--------------------------")

        self._detect_failures(cursor)
        self._detect_slow_tests(cursor)
        self._detect_browser_issues(cursor)

    def _detect_failures(self, cursor):

        cursor.execute("""
        SELECT test_name, COUNT(*) as failures
        FROM test_runs
        WHERE status='FAILED'
        GROUP BY test_name
        """)

        rows = cursor.fetchall()

        if rows:
            print("\nDetected Failures:")
            for test, count in rows:
                print(f" - {test} failed {count} times")

    def _detect_slow_tests(self, cursor):

        cursor.execute("""
        SELECT test_name, AVG(duration)
        FROM test_runs
        GROUP BY test_name
        """)

        rows = cursor.fetchall()

        print("\nAverage Test Durations:")

        for test, avg in rows:
            print(f" - {test}: {avg:.2f}s")

    def _detect_browser_issues(self, cursor):

        cursor.execute("""
        SELECT browser, COUNT(*) 
        FROM test_runs
        WHERE status='FAILED'
        GROUP BY browser
        """)

        rows = cursor.fetchall()

        if rows:
            print("\nBrowser-specific Failures:")

            for browser, count in rows:
                print(f" - {browser}: {count} failures")