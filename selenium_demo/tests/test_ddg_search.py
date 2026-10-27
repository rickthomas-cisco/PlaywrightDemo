import re

import pytest
from selenium import webdriver

from selenium_demo.pages.home import HomePage
from selenium_demo.pages.results import ResultsPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_has_title(driver):
    home = HomePage(driver)
    home.navigate()
    home.driver.save_screenshot('test-results/homepage1.png')

    assert home.get_title() == "DuckDuckGo - Protection. Privacy. Peace of mind."

def test_search_for_term_and_get_first_result(driver):
    home = HomePage(driver)
    home.navigate()
    home.search("quality assurance")

    results = ResultsPage(driver)
    duckbar = results.driver.find_element(*results.duckbar)
    duckbar.screenshot('test-results/results_duckbar.png')
    results.click_nth_result(1)
    results.driver.save_screenshot('test-results/results.png')

    assert re.match(r'.*iso\.org.*', results.get_url())