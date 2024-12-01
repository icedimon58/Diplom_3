import allure

from data import ORDERS_LINE_TEXT, CONSTRUCT_TEXT
from pages.redirect_page import RedirectPage
from pages.general_methods import GeneralMethodsPage


class TestRedirectPage:
    @allure.description('Тест перехода')
    @allure.title('Тест перехода в Ленту заказов со страницы «Личного кабинета»')
    def test_order_line_click(self, page_driver):
        redir_page = RedirectPage(page_driver)
        general_methods = GeneralMethodsPage(page_driver)
        general_methods.wait_overlay_disipearing()
        redir_page.click_order_line()
        assert redir_page.get_order_line_text() == ORDERS_LINE_TEXT

    @allure.description('Тест перехода')
    @allure.title('Тест перехода в конструктор со страницы «Личного кабинета»')
    def test_constructor_orders_click(self, page_driver):
        redir_page = RedirectPage(page_driver)
        general_methods = GeneralMethodsPage(page_driver)
        general_methods.wait_overlay_disipearing()
        redir_page.click_order_line()
        redir_page.redirect_to_condtructor()
        assert redir_page.get_construct_text() == CONSTRUCT_TEXT
