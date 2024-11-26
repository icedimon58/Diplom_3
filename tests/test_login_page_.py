import allure
from pages.login_page import LoginPage
from data import USER_MAIL, USER_PASS


class TestLoginPage:
    @allure.description('ВВодим пароль и просматриваем его')
    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным')
    def test_show_password_button(self, page_driver):
        login_page = LoginPage(page_driver)
        login_page.wait_overlay_disipearing()
        login_page.redir_to_login_page()
        login_page.fill_password_data(USER_PASS)
        assert login_page.click_on_show_pass_button() == True

    @allure.description('Проверка авторизации')
    @allure.title('Тест авторизации в «Личный кабинет»')
    def test_login_positive(self, page_driver):
        login_page = LoginPage(page_driver)
        login_page.wait_overlay_disipearing()
        login_page.redir_to_login_page()
        login_page.fill_email_data(USER_MAIL)
        login_page.fill_password_data(USER_PASS)
        login_page.login_btn_click()
        assert login_page.check_redirection() == True
