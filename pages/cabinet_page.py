import allure

from locators.cabinet_page_locators import HISTORY_BTN, LOAD_TEXT, EXIT_BTN, USERS_ORDER_IN_HISTORY
from pages.base_page import BasePage


class CabinetPage(BasePage):
    @allure.step('Переход на страницу Истории заказов')
    def click_on_history_button(self):
        self._click_on_element(HISTORY_BTN)

    @allure.step('Поиск заказа в Истории')
    def find_order_in_user_history(self):
        return self._get_element_text(USERS_ORDER_IN_HISTORY)

    @allure.step('Клик по Кнопке "Выйти"')
    def log_out(self):
        self._click_on_element(EXIT_BTN)

    @allure.step('Получение текста со страницы')
    def get_load_text(self):
        return self._wait_elem_visible(LOAD_TEXT).is_displayed()
