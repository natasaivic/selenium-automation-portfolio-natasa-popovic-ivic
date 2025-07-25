import pytest

from page_objects.context_menu_page import ContextMenuPage
from page_objects.elemental_selenium_page import elementalSeleniumPage
from page_objects.landing_page import LandingPage


@pytest.mark.smoke
class TestContextMenuPage:
    def test_context_menu_page_load_success(self, driver):
        # Go to webpage
        landing_page = LandingPage(driver)
        landing_page.open()

        # Click on Context Menu link
        landing_page.click_context_menu_link()

        # Verify page is on Context Menu
        context_menu_page = ContextMenuPage(driver)
        context_menu_page.context_menu_page_loaded_successfully()

        # Click and land on Elemental Selenium
        elemental_selenium = elementalSeleniumPage(driver)
        elemental_selenium.elemental_landing_page()