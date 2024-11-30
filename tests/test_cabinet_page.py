import allure

from pages.cabinet_page import CabinetPage
from pages.redirect_page import RedirectPage
from pages.general_methods import GeneralMethodsPage
from pages.login_page import LoginPage
from data import USER_MAIL, USER_PASS


class TestCabinetPage:

    @allure.description('Клик по кнопке перехода в историю заказов')
    @allure.title('Тест перехода в историю заказов')
    def test_click_history_btn(self, page_driver):
        cabinet_page = CabinetPage(page_driver)
        general_methods = GeneralMethodsPage(page_driver)
        redir_page = RedirectPage(page_driver)
        login_page = LoginPage(page_driver)
        redir_page.redirect_to_login_page()
        general_methods.wait_overlay_disipearing()
        redir_page.redirect_to_login_page()
        login_page.fill_email_data(USER_MAIL)
        login_page.fill_password_data(USER_PASS)
        login_page.login_btn_click()
        redir_page.redirect_to_login_page()
        general_methods.wait_overlay_disipearing()
        cabinet_page.click_on_history_button()
        assert cabinet_page.get_load_text()

    @allure.description('Производим авторизацию и выход по кнопке Выйти')
    @allure.title('Проверка выхода из аккаунта')
    def test_logout_btn(self, page_driver):
        cabinet_page = CabinetPage(page_driver)
        general_methods = GeneralMethodsPage(page_driver)
        redir_page = RedirectPage(page_driver)
        login_page = LoginPage(page_driver)
        general_methods.wait_overlay_disipearing()
        redir_page.redirect_to_login_page()
        login_page.fill_email_data(USER_MAIL)
        login_page.fill_password_data(USER_PASS)
        login_page.login_btn_click()
        redir_page.redirect_to_login_page()
        general_methods.wait_overlay_disipearing()
        cabinet_page.log_out()
        assert login_page.check_login_btn()
