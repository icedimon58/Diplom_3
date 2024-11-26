import allure

from locators.order_page_locator import ORDER_NUMBER_LOCATOR, ORDER_LOCATOR, ORDER_TEXT_LOCATOR, \
    USERS_ORDER_IN_MAIN_LIST, ORDERS_DONE_FOR_ALL_TIME, ORDERS_DONE_TODAY, ORDERS_IN_WORK, ORDER_READY_LOCATOR
from pages.base_page import BasePage
from pages.cabinet_page import CabinetPage
from pages.general_methods import GeneralMethodsPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.redirect_page import RedirectPage


class OrderPage(CabinetPage, LoginPage, RedirectPage, MainPage, GeneralMethodsPage, BasePage):
    @allure.step('Получаем количество заказов за все время')
    def get_orders_for_all_time(self):
        return self._get_element_text(ORDERS_DONE_FOR_ALL_TIME)

    @allure.step('Получаем количество заказов за все сегодня')
    def get_orders_for_today(self):
        self._find_element_on_page(ORDERS_DONE_TODAY)
        return self._get_element_text(ORDERS_DONE_TODAY)

    @allure.step('Получаем количество заказов в работе')
    def get_orders_in_work(self):
        return self._get_element_text(ORDERS_IN_WORK)

    @allure.step('Получаем текст заказа')
    def get_order_text(self):
        return self._get_element_text(ORDER_LOCATOR)

    @allure.step('Получаем текст заказа')
    def get_order_text_info(self):
        return self._get_element_text(ORDER_TEXT_LOCATOR)

    @allure.step('Получаем номер заказа')
    def get_order_number(self):
        self._wait_elem_invisible(ORDER_READY_LOCATOR)
        return self._get_element_text(ORDER_NUMBER_LOCATOR)

    @allure.step('Кликаем по заказу')
    def get_order_info(self):
        self._click_on_element(ORDER_LOCATOR)

    @allure.step('Получаем список заказов в работе')
    def find_user_order_in_orders(self):
        return self._get_element_text(USERS_ORDER_IN_MAIN_LIST)
