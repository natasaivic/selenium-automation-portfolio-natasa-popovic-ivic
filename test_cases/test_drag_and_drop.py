import pytest

from page_objects.drag_and_drop_page import DragAndDropPage
from page_objects.elemental_selenium_page import elementalSeleniumPage
from page_objects.landing_page import LandingPage


@pytest.mark.smoke
class TestDragandDrop:
    def test_drag_and_drop_page_load_success(self, driver):
        # Go to website
        landing_page = LandingPage(driver)
        landing_page.open()

        # Click on Drag and Drop link
        landing_page.click_drag_and_drop_link()

        # Verify page is on Drag and Drop
        drag_and_drop_page = DragAndDropPage(driver)
        drag_and_drop_page.drag_and_drop_page_loaded_successfully()

        # Click and land on Elemental Selenium
        elemental_selenium = elementalSeleniumPage(driver)
        elemental_selenium.elemental_landing_page()