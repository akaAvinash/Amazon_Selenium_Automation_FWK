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
        """Combined step: type & click search"""
        self.enter_search_term(term)
        self.click_search_button()

    def get_entered_search_term(self):
        """Get the value typed in the search box"""
        return self.driver.find_element(*self.SEARCH_BOX).get_attribute("value")
