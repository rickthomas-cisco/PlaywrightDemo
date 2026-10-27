from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_box = page.get_by_placeholder("Search privately")

    def navigate(self):
        self.page.goto("https://duckduckgo.com")

    def search(self, query):
        self.search_box.fill(query)
        self.search_box.press("Enter")
