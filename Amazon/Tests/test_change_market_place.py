import time
import pytest
from Amazon.Utils.Custom_logger import LogGen
from Amazon.Pages.Homepage import HomePage

logger = LogGen.init_logger(__file__)
logger.info("======================= START: test_change_market_place =============================")

def test_change_market_place(driver, request):
    homepage = HomePage(driver)
    request.node.driver = driver

    try:
        logger.info("Step 1: Clicking on the marketplace button...")
        homepage.click_on_market_place_button()

        logger.info("Step 2: Waiting for language options to load...")
        time.sleep(3)

        logger.info("Step 3: Selecting Malayalam language (value='ml_IN')...")
        homepage.click_language_by_value("ml_IN")

        logger.info("Step 4: Clicking the confirm button to apply the language change...")
        homepage.click_lang_confirm()

        logger.info("Step 5: Waiting for language change to take effect...")
        time.sleep(3)

        logger.info("Language change to Malayalam completed successfully.")

    except Exception as e:
        logger.error(f"Test failed due to unexpected error: {e}")
        raise
