import pytest

from page_objects.dynamic_loading_page import DynamicLoadingPage
from page_objects.elemental_selenium_page import elementalSeleniumPage


@pytest.mark.smoke
class TestDynamicLoadingPage:
    def test_dynamic_loading_page_load_success(self, driver):
        # Open dynamic loading page
        dynamic_loading_page = DynamicLoadingPage(driver)
        dynamic_loading_page.open()

        # Verify page loaded successfully
        dynamic_loading_page.dynamic_loading_page_loaded_successfully()
        assert dynamic_loading_page.get_page_header_text() == "Dynamically Loaded Page Elements", "Page header is not 'Dynamically Loaded Page Elements'"
        assert "dynamic_loading" in dynamic_loading_page.current_url, "Not on dynamic loading page"

        # Click and land on Elemental Selenium
        elemental_selenium = elementalSeleniumPage(driver)
        elemental_selenium.elemental_landing_page()