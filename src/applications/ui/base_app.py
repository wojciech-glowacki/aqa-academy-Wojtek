from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class BaseApp:

    def __init__(self, browser) -> None:
        self.browser = browser

    def navigate_to(self, url):
        self.browser.get(url)

    def wait_and_click(self, locator, timeout=15):
        element = self.browser.find_element(By.XPATH, locator)
        element.click()
        return True

    def enter_text(self, locator, text):
        element = self.browser.find_element(By.XPATH, locator)
        element.clear()
        element.send_keys(text)

        if element.get_attribute("value") != text:
            raise RuntimeError(
                f"Text {text} is not enetered in {locator}. Text in locator: {element.get_attribute("value")}"
            )
        # element.send_keys(Keys.RETURN)
        return True

    def check_text(self, locator, text):
        element = self.browser.find_element(By.XPATH, locator)
        return element.text == text

    def close_browser(self):
        self.browser.close()
