from Amazon.Utils.Constants import Amazon
from Amazon.Utils.Custom_logger import LogGen
from Amazon.Pages.Homepage import HomePage

logger = LogGen.init_logger(__file__)
logger.info("======================= START: test_search_playstation =============================")

def test_search_playstation(driver, request):
    amazon = Amazon()
    homepage = HomePage(driver)
    request.node.driver = driver

    try:
        logger.info("Launching Amazon Homepage")

        logger.info(f"Entering search term: {amazon.PLAY_STATION_5}")
        homepage.enter_search_term(amazon.PLAY_STATION_5)
        entered_value = homepage.get_entered_search_term()
        assert entered_value == amazon.PLAY_STATION_5, f"Entered text is not same as displayed text. Got: {entered_value}"

        logger.info("Search box input verified successfully.")

    except AssertionError as ae:
        logger.error(f"Assertion failed: {ae}")
        raise

    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        raise

    finally:
        logger.info("========== END: test_search ==========\n")
