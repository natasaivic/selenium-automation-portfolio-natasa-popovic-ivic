import pytest

from page_objects.disappearing_elements_page import DisappearingElementsPage
from page_objects.elemental_selenium_page import elementalSeleniumPage
from page_objects.landing_page import LandingPage


@pytest.mark.smoke
class TestDisappearingElementsPage:
    def test_disappearing_elements_page_load_success(self, driver):
        # Go to website
        landing_page = LandingPage(driver)
        landing_page.open()

        # Click on Disappearing Elements link
        landing_page.click_disappearing_elements_link()

        # Verify page is on Disappearing Elements
        disappearing_elements_page = DisappearingElementsPage(driver)
        disappearing_elements_page.disappearing_elements_page_loaded_successfully()

        # Click and land on Elemental Selenium
        elemental_selenium = elementalSeleniumPage(driver)
        elemental_selenium.elemental_landing_page()
