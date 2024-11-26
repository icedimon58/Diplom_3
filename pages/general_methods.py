import allure

from locators.general_methods_locators import OVERLAY_LOCATOR
from pages.base_page import BasePage


class GeneralMethodsPage(BasePage):

    @allure.step('Ждем когда пропадет оверлей')
    def wait_overlay_disipearing(self):
        self._wait_elem_invisible(OVERLAY_LOCATOR)
