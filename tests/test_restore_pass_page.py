import allure
from pages.password_restore_page import PasswordRestorePage
from data import RESTORE_PASSWORD_TEXT, USER_MAIL


class TestRestorePassPage:
    @allure.description('Тест перехода на страницу восстановления пароля')
    @allure.title('Проверка переходa на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_restore_pwd_page(self, page_driver):
        pass_restore_page = PasswordRestorePage(page_driver)
        pass_restore_page.wait_overlay_disipearing()
        pass_restore_page.redirect_to_login_page()
        pass_restore_page.click_restore_password_link()
        assert pass_restore_page.find_restore_password_text() == RESTORE_PASSWORD_TEXT

    @allure.description('Проверка восстановления пароля')
    @allure.title('Проверка ввода почты и клик по кнопке «Восстановить»')
    def test_mail_password_fields_page(self, page_driver):
        pass_restore_page = PasswordRestorePage(page_driver)
        pass_restore_page.wait_overlay_disipearing()
        pass_restore_page.redirect_to_login_page()
        pass_restore_page.click_restore_password_link()
        pass_restore_page.fill_email_data(USER_MAIL)
        pass_restore_page.click_restore_password_button()
        assert pass_restore_page.find_restore_password_text() == RESTORE_PASSWORD_TEXT
