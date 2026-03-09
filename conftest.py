import pytest
import time
from playwright.sync_api import sync_playwright

from analytics.metrics_store import MetricsStore
from core.artifact_manager import ArtifactManager
from chaos.network_chaos import NetworkChaos
from chaos.failure_injection import FailureInjector

metrics_store = MetricsStore()


def pytest_addoption(parser):

    parser.addoption(
        "--network",
        action="store",
        default="normal",
        help="Network mode for chaos testing"
    )

    parser.addoption(
        "--failure",
        action="store",
        default="none",
        help="Failure injection mode"
    )


def launch_browser(playwright, browser_name):

    if browser_name == "chromium":
        return playwright.chromium.launch(headless=True)

    if browser_name == "firefox":
        return playwright.firefox.launch(headless=True)

    if browser_name == "webkit":
        return playwright.webkit.launch(headless=True)

    raise ValueError(f"Unsupported browser: {browser_name}")


@pytest.fixture(params=["chromium", "firefox", "webkit"])
def browser_context(request):

    network_mode = request.config.getoption("--network")
    failure_mode = request.config.getoption("--failure")
    browser_name = request.param

    artifact_manager = ArtifactManager(browser_name)

    with sync_playwright() as p:

        browser = launch_browser(p, browser_name)

        context = browser.new_context(
            record_video_dir=artifact_manager.video_dir
        )

        chaos = NetworkChaos(context)
        chaos.apply(network_mode)

        injector = FailureInjector(context)
        injector.apply(failure_mode)

        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        page = context.new_page()

        start_time = time.time()

        yield page

        duration = time.time() - start_time

        test_name = request.node.name
        trace_file = artifact_manager.generate_filename(test_name, "zip")

        context.tracing.stop(
            path=f"{artifact_manager.trace_dir}/{trace_file}"
        )

        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":

        browser = item.callspec.params.get("browser_context", "unknown")

        if rep.passed:
            metrics_store.record_test(browser, True)

        else:
            metrics_store.record_test(browser, False)

            page = item.funcargs.get("browser_context")

            if page:
                artifact_manager = ArtifactManager(browser)
                artifact_manager.capture_screenshot(page, item.name)