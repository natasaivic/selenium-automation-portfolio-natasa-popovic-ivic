import pytest

from page_objects.challenging_dom_page import ChallengingDomPage
from page_objects.elemental_selenium_page import elementalSeleniumPage
from page_objects.landing_page import LandingPage


@pytest.mark.smoke
class TestChallengingDomPage:
    def test_challenging_dom_page_load_success(self, driver):
        # Go to webpage
        landing_page = LandingPage(driver)
        landing_page.open()

        # Click on Challenging DOM link
        landing_page.click_challenging_dom_link()

        # Verify page is on Challenging DOM
        challenging_dom_page = ChallengingDomPage(driver)
        challenging_dom_page.challenging_dom_page_loaded_successfully()

        # Click and land on Elemental Selenium
        elemental_selenium = elementalSeleniumPage(driver)
        elemental_selenium.elemental_landing_page()