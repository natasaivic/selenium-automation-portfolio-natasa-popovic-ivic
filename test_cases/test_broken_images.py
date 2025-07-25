import pytest

from page_objects.broken_images_page import BrokenImagesPage
from page_objects.elemental_selenium_page import elementalSeleniumPage
from page_objects.landing_page import LandingPage


@pytest.mark.smoke
class TestBrokenImagesPage:
    def test_broken_images_page_load_success(self, driver):
        # Go to webpage
        landing_page = LandingPage(driver)
        landing_page.open()

        # Click on Broken Images link
        landing_page.click_broken_images_link()

        # Verify page is on Broken Images
        broken_images_page = BrokenImagesPage(driver)
        broken_images_page.broken_images_page_loaded_successfully()

        # Click and land on Elemental Selenium
        elemental_selenium = elementalSeleniumPage(driver)
        elemental_selenium.elemental_landing_page()