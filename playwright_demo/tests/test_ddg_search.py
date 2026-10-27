import re

from playwright.sync_api import expect, Page

from playwright_demo.pages.home import HomePage
from playwright_demo.pages.results import ResultsPage

def test_has_title(page: Page):
    home = HomePage(page)
    home.navigate()
    home.page.screenshot(path='test-results/homepage1.png')

    expect(home.page).to_have_title("DuckDuckGo - Protection. Privacy. Peace of mind.")

def test_search_for_term_and_get_first_result(page: Page):
    home = HomePage(page)
    home.navigate()
    home.search("quality assurance")

    results = ResultsPage(page)
    results.duckbar.screenshot(path='test-results/results_duckbar.png')
    results.click_nth_result(1)
    results.page.screenshot(path='test-results/results.png')

    expect(results.page).to_have_url(re.compile(r'.*iso\.org.*'))
