import allure

from pages.base_page import BasePage
from locators.restore_pwd_page_locators import RESTORE_PASS_PAGE_TEXT, RESTORE_BTN, RESTORE_PSWD_LINK, \
    RESTORE_PASS_EMAIL_FIELD


class PasswordRestorePage(BasePage):

    @allure.step('Клик по кнопке Восстановить пароль')
    def click_restore_password_button(self):
        self.redirect_to(RESTORE_BTN)

    @allure.step('Клик по ссылке Восстановить пароль')
    def click_restore_password_link(self):
        self.redirect_to(RESTORE_PSWD_LINK)

    @allure.step('Переход по элементу')
    def redirect_to(self, locator):
        self._click_on_element(locator)

    @allure.step('Заполнение поля email')
    def fill_email_data(self, email):
        self._find_element_on_page(RESTORE_PASS_EMAIL_FIELD)
        self._set_element_text(RESTORE_PASS_EMAIL_FIELD, email)

    @allure.step('Поиск текста страницы')
    def find_restore_password_text(self):
        return self._get_element_text(RESTORE_PASS_PAGE_TEXT)
