from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Amazon.Utils.Constants import Amazon

class HomePage:
    def __init__(self,driver):
        self.driver = driver
        self.amazon = Amazon

    # Locators
    SEARCH_BOX = (By.ID,Amazon.SEARCH_BOX)
    SEARCH_BUTTON = (By.ID,Amazon.SEARCH_BUTTON)
    MARKET_PLACE_BUTTON = (By.XPATH,Amazon.MARKET_PLACE_BUTTON)
    MALAYALAM_LANG_BUTTON = (By.XPATH, Amazon.MALAYALAM_LANG)
    LANG_CONFIRM_BUTTON = (By.CSS_SELECTOR,Amazon.LANG_CONFIRM)

    # Actions
    def enter_search_term(self,term):
        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.SEARCH_BOX)
        ).send_keys(term)

    def click_search_button(self,term):
        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.SEARCH_BUTTON)
        ).click()

    def search_product(self, term):
        """Combined step: type and click search"""
        self.enter_search_term(term)
        self.click_search_button()

    def get_entered_search_term(self):
        """Get the value typed in the search box"""
        return self.driver.find_element(*self.SEARCH_BOX).get_attribute("value")

    def click_on_market_place_button(self):
        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.MARKET_PLACE_BUTTON)
        ).click()

    def click_language_by_value(self, lang_value):
        # Wait for all language input elements to be present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, Amazon.LANG_OPTIONS))
        )

        radio_inputs = self.driver.find_elements(By.XPATH, Amazon.LANG_OPTIONS)

        for input_elem in radio_inputs:
            try:
                value = input_elem.get_attribute("value")
                if value == lang_value:
                    icon_elem = input_elem.find_element(By.XPATH, "following-sibling::i")
                    icon_elem.click()
                    return
            except Exception as e:
                continue

        raise Exception(f"Language with value '{lang_value}' not found.")

    def click_lang_confirm(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LANG_CONFIRM_BUTTON)
        ).click()