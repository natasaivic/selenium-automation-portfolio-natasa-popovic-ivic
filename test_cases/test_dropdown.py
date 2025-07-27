import pytest

from page_objects.dropdown_page import DropdownPage
from page_objects.elemental_selenium_page import elementalSeleniumPage


@pytest.mark.smoke
class TestDropdownPage:
    def test_dropdown_page_load_success(self, driver):
        # Open dropdown page
        dropdown_page = DropdownPage(driver)
        dropdown_page.open()

        # Verify page loaded successfully
        dropdown_page.dropdown_page_loaded_successfully()
        assert dropdown_page.get_page_header_text() == "Dropdown List", "Page header is not 'Dropdown List'"
        assert "dropdown" in dropdown_page.current_url, "Not on dropdown page"

        # Click and land on Elemental Selenium
        elemental_selenium = elementalSeleniumPage(driver)
        elemental_selenium.elemental_landing_page()