import pytest

from page_objects.digest_authentication_page import DigestAuthenticationPage
from page_objects.elemental_selenium_page import elementalSeleniumPage
from page_objects.landing_page import LandingPage


@pytest.mark.smoke
class TestDigestAuthPage:
    def test_digest_auth_page_load_success(self, driver):
        # Open digest auth page with valid credentials to avoid authentication popup
        digest_auth_page = DigestAuthenticationPage(driver)
        digest_auth_page.open_with_credentials("admin", "admin")

        # Verify successful authentication and page load
        digest_auth_page.digest_auth_page_loaded_successfully()
        assert digest_auth_page.is_authenticated_successfully(), "Digest authentication failed"
        assert "digest_auth" in digest_auth_page.current_url, "Not on digest auth page"

        # Click and land on Elemental Selenium
        elemental_selenium = elementalSeleniumPage(driver)
        elemental_selenium.elemental_landing_page()