# from Amazon.Utils.Constants import Amazon
# from Amazon.Utils.Custom_logger import LogGen
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# logger = LogGen.init_logger(__file__)
# logger.info("========== START: test_search_iPhone ==========")
#
# def test_search(driver, request):
#     amazon = Amazon()
#     request.node.driver = driver  # For screenshot on failure (if used)
#
#     try:
#         logger.info("Launching Amazon homepage...")
#
#         logger.info(f"Waiting for search box (ID: {amazon.SEARCH_BOX}) to be visible")
#         search_box = WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.ID, amazon.SEARCH_BOX))
#         )
#
#         logger.info(f"Typing search term: '{amazon.IPHONE}'")
#         search_box.send_keys(amazon.IPHONE)
#
#         entered_value = search_box.get_attribute("value")
#         logger.debug(f"Entered value in search box: '{entered_value}'")
#         assert entered_value == amazon.IPHONE, f"Entered text does not match. Got: {entered_value}"
#         logger.info("Search input verified.")
#
#         logger.info("Clicking search button...")
#         driver.find_element(By.ID, amazon.SEARCH_BUTTON).click()
#
#         logger.info("Waiting for Apple logo to appear on the results page...")
#         apple_logo = WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, amazon.APPLE_LOGO))
#         )
#         assert apple_logo.is_displayed(), "Apple logo not found on search results page"
#         logger.info("Apple logo is visible. Search results loaded successfully.")
#
#     except AssertionError as ae:
#         logger.error(f"Assertion failed: {ae}")
#         raise
#
#     except Exception as e:
#         logger.error(f"Unexpected error occurred: {e}")
#         raise
#
#     finally:
#         logger.info("========== END: test_search ==========\n")
