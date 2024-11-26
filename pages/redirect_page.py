import allure

from locators.redirect_page_locators import KABINET_LOCATOR, ORDERS_LINE, CONSTRUCT_LINE_BTN, ORDERS_LINE_HEADER, \
    OVERLAY_LOAD_LOCATOR_REDIR_PAGE, ORDER_LINE_TEXT_REDIR_PAGE, CONSTRUCT_LINE_TEXT_REDIR_PAGE
from pages.base_page import BasePage
from pages.general_methods import GeneralMethodsPage
from pages.main_page import MainPage


class RedirectPage(MainPage, GeneralMethodsPage, BasePage):

    @allure.step('Переход на страницу авторизации')
    def redirect_to_login_page(self):
        self._wait_elem_invisible(OVERLAY_LOAD_LOCATOR_REDIR_PAGE)
        self._click_on_element(KABINET_LOCATOR)

    @allure.step('Переход на Ленту заказов')
    def redirect_to_orders(self):
        self._wait_elem_invisible(OVERLAY_LOAD_LOCATOR_REDIR_PAGE)
        self._click_on_element(ORDERS_LINE)

    @allure.step('Переход к конструктору')
    def redirect_to_condtructor(self):
        self._wait_elem_invisible(OVERLAY_LOAD_LOCATOR_REDIR_PAGE)
        self._click_on_element(CONSTRUCT_LINE_BTN)

    @allure.step('Переход по элементу')
    def redirect_to(self, locator):
        self._click_on_element(locator)

    @allure.step('Переход на старницу заказов')
    def click_order_line(self):
        self._click_on_element(ORDERS_LINE_HEADER)

    @allure.step('Получение текста со тсраницы Заказов')
    def get_order_line_text(self):
        return self._get_element_text(ORDER_LINE_TEXT_REDIR_PAGE)

    @allure.step('Получение текста со тсраницы Конструктора')
    def get_construct_text(self):
        return self._get_element_text(CONSTRUCT_LINE_TEXT_REDIR_PAGE)
