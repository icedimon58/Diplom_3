import allure

from locators.redirect_page_locators import KABINET_LOCATOR
from pages.base_page import BasePage
from locators.login_page_locators import MAIL_FIELD, PASSWORD_FIELD, PASSWORD_SHOW_BUTTON, FILLED_LOCATOR, LOGIN_BUTTON


class LoginPage(BasePage):

    @allure.step('Ждем когда появится локатор Личной страницы')
    def check_redirection(self):
        return self._wait_elem_visible(KABINET_LOCATOR).is_displayed()

    @allure.step('Проверка что кнопка Авторизации появилась')
    def check_login_btn(self):
        return self._wait_elem_visible(LOGIN_BUTTON).is_displayed()

    @allure.step('Клик по кнопке Авторизации')
    def login_btn_click(self):
        self._click_on_element(LOGIN_BUTTON)

    @allure.step('Клик по кнопке "Показать пароль"')
    def click_on_show_pass_button(self):
        self._click_on_element(PASSWORD_SHOW_BUTTON)
        return self._wait_elem_visible(FILLED_LOCATOR).is_displayed()

    @allure.step('Заполняем поле "Пароль"')
    def fill_password_data(self, pwd):
        self._set_element_text(PASSWORD_FIELD, pwd)

    @allure.step('Заполняем поле "email"')
    def fill_email_data(self, email):
        self._set_element_text(MAIL_FIELD, email)
