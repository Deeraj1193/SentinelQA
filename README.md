# SentinelQA

**SentinelQA** is an automated QA testing platform designed for **web application testing**.
It executes automated browser tests, collects debugging artifacts, analyzes test stability, and provides a **dashboard for test analytics**.

---

# Features

SentinelQA provides multiple QA testing capabilities:

* Cross-browser testing (**Chromium, Firefox, WebKit**)
* Parallel test execution
* End-to-end automated testing
* Chaos testing (**network and failure injection**)
* Visual regression testing
* Flaky test detection
* Artifact collection (**screenshots, videos, traces**)
* Analytics dashboard for test insights

---

# Architecture

SentinelQA consists of four main components:

```
SentinelQA
│
├── core/
│   ├── test_runner
│   └── artifact_manager
│
├── analytics/
│   ├── metrics_collection
│   ├── visual_regression
│   └── flaky_test_detection
│
├── chaos/
│   ├── network_chaos
│   └── failure_injection
│
└── dashboard/
    └── test_analytics_dashboard
```

---

# Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOURNAME/SentinelQA
cd SentinelQA
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

---

# Running Tests

### Run SentinelQA

```bash
python sentinel.py
```

### Run with Parallel Workers

```bash
python sentinel.py --workers 3
```

### Run with Network Chaos

```bash
python sentinel.py --network slow
```

### Run with Failure Injection

```bash
python sentinel.py --failure js_error
```

---

# Dashboard

Start the analytics dashboard:

```bash
python dashboard/app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

The dashboard provides:

* Test metrics
* Failure screenshots
* Browser distribution
* Pass/fail analytics

---

# Artifacts

SentinelQA automatically stores test artifacts:

```
artifacts/
├── chromium/
├── firefox/
└── webkit/
```

Artifacts include:

* Screenshots
* Playwright traces
* Video recordings

These artifacts help **debug failed tests**.

---

# Example Use Case

SentinelQA can be used to:

* Test web applications across multiple browsers
* Simulate unstable network conditions
* Detect UI regressions
* Identify flaky tests
* Analyze failures through captured artifacts

---

# Roadmap

Future improvements planned:

* AI-assisted failure analysis
* Artifact explorer dashboard
* Prometheus / Grafana metrics support
* CI/CD integration

---

# Tech Stack

* Python
* Playwright
* PyTest
* Flask
* Chart.js
* Docker

---