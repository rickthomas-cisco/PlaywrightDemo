from playwright.sync_api import Page

class ResultsPage:
    def __init__(self, page: Page):
        self.page = page
        self.duckbar = page.get_by_test_id("duckbar")
        self.mainline = page.get_by_test_id("mainline")
        self.more_results_button = page.get_by_role("button", name="More Results")

    def show_all_results(self):
        self.duckbar.get_by_role("listitem").filter(has_text="All").click()

    def show_image_results(self):
        self.duckbar.get_by_role("listitem").filter(has_text="Images").click()

    def show_video_results(self):
        self.duckbar.get_by_role("listitem").filter(has_text="Videos").click()

    def show_news_results(self):
        self.duckbar.get_by_role("listitem").filter(has_text="News").click()

    def show_more_results(self):
        self.more_results_button.click()

    def click_nth_result(self, n):
        self.mainline.get_by_role("listitem").nth(n).click()
