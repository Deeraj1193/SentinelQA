from flask import Flask, render_template, jsonify, send_from_directory
import json
import os

app = Flask(__name__)

METRICS_FILE = "analytics/metrics.json"


def load_metrics():
    with open(METRICS_FILE) as f:
        return json.load(f)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/metrics")
def metrics():
    return jsonify(load_metrics())

@app.route("/screenshots")
def screenshots():

    screenshots = []

    base = "artifacts"

    for browser in os.listdir(base):

        folder = os.path.join(base, browser, "screenshots")

        if not os.path.exists(folder):
            continue

        for file in os.listdir(folder):
            screenshots.append({
                "browser": browser,
                "file": file
            })

    return jsonify(screenshots)


@app.route("/artifacts/<browser>/screenshots/<path:filename>")
def artifact(browser, filename):

    base_dir = os.path.dirname(os.path.dirname(__file__))

    folder = os.path.join(base_dir, "artifacts", browser, "screenshots")

    return send_from_directory(folder, filename)


if __name__ == "__main__":
    app.run(debug=True)