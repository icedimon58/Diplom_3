import allure

from locators.cabinet_page_locators import HISTORY_BTN, LOAD_TEXT, EXIT_BTN, USERS_ORDER_IN_HISTORY
from pages.base_page import BasePage
from pages.general_methods import GeneralMethodsPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.redirect_page import RedirectPage


class CabinetPage(LoginPage, RedirectPage, MainPage, GeneralMethodsPage, BasePage):
    @allure.step('Переход на страницу Истории заказов')
    def click_on_history_button(self):
        self.wait_overlay_disipearing()
        self._click_on_element(HISTORY_BTN)

    @allure.step('Поиск заказа в Истории')
    def find_order_in_user_history(self):
        return self._get_element_text(USERS_ORDER_IN_HISTORY)

    @allure.step('Клик по Кнопке "Выйти"')
    def log_out(self):
        self.wait_overlay_disipearing()
        self._click_on_element(EXIT_BTN)

    @allure.step('Получение текста со страницы')
    def get_load_text(self):
        return self._wait_elem_visible(LOAD_TEXT).is_displayed()
