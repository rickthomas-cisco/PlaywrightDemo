from selenium.webdriver.common.by import By

from selenium_demo.pages.base import BasePage


class ResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.duckbar = (By.CSS_SELECTOR, "[data-testid='duckbar']")
        self.mainline = (By.CSS_SELECTOR, "[data-testid='mainline']")
        self.results = (By.CLASS_NAME, "react-results--main")
        self.more_results_button = (By.XPATH, "//button[contains(text(), 'More Results')]")

    def show_all_results(self):
        all_results = self.driver.find_element(*self.duckbar).find_element(By.XPATH, ".//li[contains(text(), 'All')]")
        all_results.click()

    def show_image_results(self):
        image_results = self.driver.find_element(*self.duckbar).find_element(By.XPATH, ".//li[contains(text(), 'Images')]")
        image_results.click()

    def show_video_results(self):
        video_results = self.driver.find_element(*self.duckbar).find_element(By.XPATH, ".//li[contains(text(), 'Videos')]")
        video_results.click()

    def show_news_results(self):
        news_results = self.driver.find_element(*self.duckbar).find_element(By.XPATH, ".//li[contains(text(), 'News')]")
        news_results.click()

    def show_more_results(self):
        self.click(self.more_results_button)

    def click_nth_result(self, n):
        nth_result = self.driver.find_element(*self.results).find_elements(By.TAG_NAME, "li")[n]
        nth_result.click()