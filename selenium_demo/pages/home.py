from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium_demo.pages.base import BasePage

class HomePage(BasePage):
    search_box = (By.NAME, "q")
    def __init__(self, driver):
        super().__init__(driver)

    def navigate(self):
        self.driver.get("https://duckduckgo.com")

    def search(self, query):
        self.send_keys(self.search_box, query)
        self.send_keys(self.search_box, Keys.ENTER)
