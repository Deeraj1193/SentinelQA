import sys
import subprocess
import os


def main():

    if len(sys.argv) < 2:
        print("Usage: python view_trace.py <trace_file>")
        return

    trace_file = sys.argv[1]

    if not os.path.exists(trace_file):
        print("Trace file not found:", trace_file)
        return

    print("Opening Playwright Trace Viewer...")

    subprocess.run([
        "npx",
        "playwright",
        "show-trace",
        trace_file
    ])


if __name__ == "__main__":
    main()