from selenium import webdriver
from Amazon.Utils.Constants import Amazon

class Helper:

    def __init__(self):
        self.target_url = Amazon.TARGET_URL
        self.driver = None

    def get_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.target_url)
        self.driver.maximize_window()
        return self.driver
