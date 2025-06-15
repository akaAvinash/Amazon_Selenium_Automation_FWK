from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Helper:
    def __init__(self):
        self.driver = None
        self.target_url = "https://www.amazon.in"  # Or whatever your default URL is

    def get_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-dev-tools")
        chrome_options.add_argument("--remote-debugging-port=9222")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(self.target_url)
        self.driver.maximize_window()
        return self.driver