import allure

from data import ORDERS_LINE_TEXT, CONSTRUCT_TEXT
from pages.redirect_page import RedirectPage


class TestRedirectPage:
    @allure.description('Тест перехода')
    @allure.title('Тест перехода в Ленту заказов со страницы «Личного кабинета»')
    def test_order_line_click(self, page_driver):
        header_page = RedirectPage(page_driver)
        header_page.wait_overlay_disipearing()
        header_page.click_order_line()
        assert header_page.get_order_line_text() == ORDERS_LINE_TEXT

    @allure.description('Тест перехода')
    @allure.title('Тест перехода в конструктор со страницы «Личного кабинета»')
    def test_constructor_orders_click(self, page_driver):
        header_page = RedirectPage(page_driver)
        header_page.wait_overlay_disipearing()
        header_page.click_order_line()
        header_page.redirect_to_condtructor()
        assert header_page.get_construct_text() == CONSTRUCT_TEXT
