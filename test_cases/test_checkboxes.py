import pytest

from page_objects.checkboxes_page import CheckboxesPage
from page_objects.elemental_selenium_page import elementalSeleniumPage
from page_objects.landing_page import LandingPage


@pytest.mark.smoke
class TestCheckboxesPage:
    def test_checkboxes_page_load_success(self, driver):
        # Go to website
        landing_page = LandingPage(driver)
        landing_page.open()

        # Click on Checkbox link
        landing_page.click_checkboxes_link()

        # Verify page is on Checkbox
        checkbox_page = CheckboxesPage(driver)
        checkbox_page.checkboxes_page_loaded_successfully()

        # Click and land on Elemental Selenium
        elemental_selenium = elementalSeleniumPage(driver)
        elemental_selenium.elemental_landing_page()