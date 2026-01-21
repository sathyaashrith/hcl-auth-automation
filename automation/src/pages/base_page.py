from automation.src.utils.wait_utils import WaitUtils

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.waits = WaitUtils(driver, timeout)

    def open_url(self, url):
        self.driver.get(url)

    def get_text(self, locator):
        return self.waits.wait_visible(locator).text

    def type_text(self, locator, value):
        element = self.waits.wait_visible(locator)
        element.clear()
        element.send_keys(value)

    def click(self, locator):
        self.waits.wait_clickable(locator).click()
