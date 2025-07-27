import pytest

from page_objects.dynamic_content_page import DynamicContentPage
from page_objects.elemental_selenium_page import elementalSeleniumPage


@pytest.mark.smoke
class TestDynamicContentPage:
    def test_dynamic_content_page_load_success(self, driver):
        # Open dynamic content page
        dynamic_content_page = DynamicContentPage(driver)
        dynamic_content_page.open()

        # Verify page loaded successfully
        dynamic_content_page.dynamic_content_page_loaded_successfully()
        assert dynamic_content_page.get_page_header_text() == "Dynamic Content", "Page header is not 'Dynamic Content'"
        assert "dynamic_content" in dynamic_content_page.current_url, "Not on dynamic content page"

        # Click and land on Elemental Selenium
        elemental_selenium = elementalSeleniumPage(driver)
        elemental_selenium.elemental_landing_page()