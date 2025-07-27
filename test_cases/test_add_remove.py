import pytest

from page_objects.add_remove_page import AddRemoveElementsPage
from page_objects.elemental_selenium_page import elementalSeleniumPage


@pytest.mark.smoke
class TestAddRemoveElementsPage:
    def test_add_remove_elements_page_load_success(self, driver):
        # Open add/remove elements page
        add_remove_page = AddRemoveElementsPage(driver)
        add_remove_page.open()

        # Verify page loaded successfully
        add_remove_page.add_remove_elements_page_loaded_successfully()
        assert add_remove_page.get_page_header_text() == "Add/Remove Elements", "Page header is not 'Add/Remove Elements'"
        assert "add_remove_elements" in add_remove_page.current_url, "Not on add/remove elements page"

        # Click and land on Elemental Selenium
        elemental_selenium = elementalSeleniumPage(driver)
        elemental_selenium.elemental_landing_page()