import os
import pytest
from datetime import datetime
from Amazon.Utils.Helpers import Helper

# Global to access pytest-html plugin
pytest_html = None

@pytest.fixture
def driver(request):
    helper = Helper()
    driver = helper.get_driver()

    request.node.driver = driver  # for screenshot capture on failure

    yield driver  # Give driver to the test

    driver.quit()  # Cleanly close after test

def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")

    reports_dir = os.path.join(os.path.dirname(__file__), 'Reports')
    os.makedirs(reports_dir, exist_ok=True)

    if not config.option.htmlpath:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        config.option.htmlpath = os.path.join(reports_dir, f"report_{timestamp}.html")

    screenshots_dir = os.path.join(os.path.dirname(__file__), 'Screenshots')
    os.makedirs(screenshots_dir, exist_ok=True)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" or report.when == "setup":
        driver = getattr(item, 'driver', None)
        if driver and (report.failed or report.passed):
            screenshot_dir = os.path.join(os.path.dirname(__file__), "Screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            file_name = f"{item.name}_{report.when}.png"
            file_path = os.path.join(screenshot_dir, file_name)

            driver.save_screenshot(file_path)

            if hasattr(report, "extra"):
                extra = report.extra
            else:
                extra = report.extra = []

            # Relative path for report
            rel_path = os.path.relpath(file_path, start=os.path.dirname(item.config.option.htmlpath))
            extra.append(pytest_html.extras.image(rel_path))