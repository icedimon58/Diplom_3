import allure

from pages.cabinet_page import CabinetPage
from data import USER_MAIL, USER_PASS


class TestCabinetPage:

    @allure.description('Клик по кнопке перехода в историю заказов')
    @allure.title('Тест перехода в историю заказов')
    def test_click_history_btn(self, page_driver):
        cabinet_page = CabinetPage(page_driver)
        cabinet_page.wait_overlay_disipearing()
        cabinet_page.redir_to_login_page()
        cabinet_page.fill_email_data(USER_MAIL)
        cabinet_page.fill_password_data(USER_PASS)
        cabinet_page.login_btn_click()
        cabinet_page.redir_to_login_page()
        cabinet_page.click_on_history_button()
        assert cabinet_page.get_load_text() == True

    @allure.description('Производим авторизацию и выход по кнопке Выйти')
    @allure.title('Проверка выхода из аккаунта')
    def test_logout_btn(self, page_driver):
        cabinet_page = CabinetPage(page_driver)
        cabinet_page.wait_overlay_disipearing()
        cabinet_page.redir_to_login_page()
        cabinet_page.fill_email_data(USER_MAIL)
        cabinet_page.fill_password_data(USER_PASS)
        cabinet_page.login_btn_click()
        cabinet_page.redir_to_login_page()
        cabinet_page.log_out()
        assert cabinet_page.check_login_btn() == True
