import pytest

from page_objects.dynamic_controls_page import DynamicControlsPage
from page_objects.elemental_selenium_page import elementalSeleniumPage


@pytest.mark.smoke
class TestDynamicControlsPage:
    def test_dynamic_controls_page_load_success(self, driver):
        # Open dynamic controls page
        dynamic_controls_page = DynamicControlsPage(driver)
        dynamic_controls_page.open()

        # Verify page loaded successfully
        dynamic_controls_page.dynamic_controls_page_loaded_successfully()
        assert dynamic_controls_page.get_page_header_text() == "Dynamic Controls", "Page header is not 'Dynamic Controls'"
        assert "dynamic_controls" in dynamic_controls_page.current_url, "Not on dynamic controls page"

        # Click and land on Elemental Selenium
        elemental_selenium = elementalSeleniumPage(driver)
        elemental_selenium.elemental_landing_page()