from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains

from page_objects.base_page import BasePage


class ContextMenuPage(BasePage):
    __url = "https://the-internet.herokuapp.com/context_menu"
    __page_header = (By.TAG_NAME, "h3")
    __description_text = (By.XPATH, "//p[contains(., 'Context menu items are custom additions')]")
    __instruction_text = (By.XPATH, "//p[contains(., 'Right-click in the box below')]")
    __hot_spot = (By.ID, "hot-spot")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    def context_menu_page_loaded_successfully(self):
        assert super().is_displayed(self.__page_header), "The header is not displayed"

    def is_hot_spot_displayed(self) -> bool:
        return super().is_displayed(self.__hot_spot)

    def right_click_hot_spot(self):
        hot_spot_element = super()._find(self.__hot_spot)
        actions = ActionChains(super()._driver)
        actions.context_click(hot_spot_element).perform()

    def get_alert_text(self) -> str:
        alert = super()._driver.switch_to.alert
        return alert.text

    def accept_alert(self):
        alert = super()._driver.switch_to.alert
        alert.accept()

    def dismiss_alert(self):
        alert = super()._driver.switch_to.alert
        alert.dismiss()

    def is_alert_present(self) -> bool:
        try:
            super()._driver.switch_to.alert
            return True
        except:
            return False