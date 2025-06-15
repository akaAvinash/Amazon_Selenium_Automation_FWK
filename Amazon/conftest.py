# import os
# import pytest
# from datetime import datetime
#
# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     reports_dir = os.path.join(os.path.dirname(__file__), 'Reports')
#     os.makedirs(reports_dir, exist_ok=True)
#
#     # Get the test file name from config.args (like "Tests/test_search_product.py")
#     if config.args:
#         test_file_path = config.args[0]
#         test_file_name = os.path.splitext(os.path.basename(test_file_path))[0]
#     else:
#         test_file_name = "report"
#
#     # Timestamped report filename using test file name
#     timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     report_filename = f"{test_file_name}_{timestamp}.html"
#
#     if not config.option.htmlpath:
#         config.option.htmlpath = os.path.join(reports_dir, report_filename)


# import os
# import pytest
# from datetime import datetime
# from py.xml import html
# import pytest_html
#
#
# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     global pytest_html
#     pytest_html = config.pluginmanager.getplugin("html")
#
#     reports_dir = os.path.join(os.path.dirname(__file__), 'Reports')
#     os.makedirs(reports_dir, exist_ok=True)
#
#     if not config.option.htmlpath:
#         timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#         config.option.htmlpath = os.path.join(reports_dir, f"report_{timestamp}.html")
#
#     screenshots_dir = os.path.join(os.path.dirname(__file__), 'Screenshots')
#     os.makedirs(screenshots_dir, exist_ok=True)
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     result = outcome.get_result()
#
#     if result.when == "call":
#         driver = getattr(item, "driver", None)
#
#         if driver:
#             driver = getattr(driver, "driver", None)
#
#         if not driver and hasattr(item, "function"):
#             test_obj = getattr(item.function, "__self__", None)
#             if test_obj and hasattr(test_obj, "driver"):
#                 driver = test_obj.driver
#
#         if driver:
#             screenshots_dir = os.path.join(os.path.dirname(__file__), 'Screenshots')
#             timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#             status = result.outcome
#             file_name = f"{item.name}_{status}_{timestamp}.png"
#             file_path = os.path.join(screenshots_dir, file_name)
#             rel_path = os.path.relpath(file_path, start=os.path.dirname(item.config.option.htmlpath))
#
#             try:
#                 driver.save_screenshot(file_path)
#                 if file_path and os.path.exists(file_path):
#                     extra = getattr(result, 'extra', [])
#                     extra.append(pytest_html.extras.image(rel_path))
#                     result.extra = extra
#             except Exception as e:
#                 print(f"Could not attach screenshot for {item.name}: {e}")

import os
import pytest
from datetime import datetime

# Global to access pytest-html plugin
pytest_html = None

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