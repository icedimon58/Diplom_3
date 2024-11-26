from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import SCRIPT_TEXT


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def _click_on_element(self, locator):
        (WebDriverWait(self.driver, 10).until
         (expected_conditions.element_to_be_clickable(locator)))
        self.driver.find_element(*locator).click()

    def _drag_and_drop_element(self, locator_from, locator_to):
        self.driver.execute_script(SCRIPT_TEXT, locator_from, locator_to)

    def _wait_elem_visible(self, locator):
        return (WebDriverWait(self.driver, 10).until
                (expected_conditions.visibility_of_element_located(locator)))

    def _wait_elem_invisible(self, locator):
        (WebDriverWait(self.driver, 10).until_not
         (expected_conditions.visibility_of_any_elements_located(locator)))

    def _find_element_on_page(self, locator):
        WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def _set_element_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def _get_element_text(self, locator):
        return self._find_element_on_page(locator).text
