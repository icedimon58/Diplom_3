import allure

from pages.base_page import BasePage
from pages.general_methods import GeneralMethodsPage
from locators.main_page_locators import ITEM_LOCATOR, ITEM_TEXT, CLOSE_BUTTON_LOCATOR_MAIN_PAGE, BASCET_LOCATOR, \
    INGRIDIENT_LOCATOR, TAKE_ORDER_LOCATOR, CLOSE_BUTTON_LOCATOR_OVER


class MainPage(GeneralMethodsPage, BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.before_add = None
        self.after_add = None

    @allure.step('Кликаем по ингредиенту')
    def click_on_get_ingridient(self):
        self.wait_overlay_disipearing()
        self._click_on_element(ITEM_LOCATOR)

    @allure.step('Получаем текст со страницы ингредиента')
    def get_ingridient_window_text(self):
        return self._get_element_text(ITEM_TEXT)

    @allure.step('Перетаскиваем ингредиент')
    def drag_and_drop_element(self):
        self.before_add = self._get_element_text(INGRIDIENT_LOCATOR)
        source = self._find_element_on_page(ITEM_LOCATOR)
        target = self._find_element_on_page(BASCET_LOCATOR)
        self._drag_and_drop_element(source, target)
        self.after_add = self._get_element_text(INGRIDIENT_LOCATOR)

    @allure.step('Проверяем, что изменился счетчик элементов')
    def check_drag_and_drop(self):
        if self.after_add > self.before_add:
            return True
        return False

    @allure.step('Кликаем по кнопке Оформить заказ')
    def click_take_order_button(self):
        self._click_on_element(TAKE_ORDER_LOCATOR)

    @allure.step('Проверка того, что окно  исчезло')
    def check_close_btn_invisible(self):
        return self._wait_elem_visible(CLOSE_BUTTON_LOCATOR_MAIN_PAGE).is_displayed()

    @allure.step('Закрываем окно Индгредиента')
    def close_ingredient_window(self):
        self._wait_elem_visible(CLOSE_BUTTON_LOCATOR_OVER)
        self._click_on_element(CLOSE_BUTTON_LOCATOR_MAIN_PAGE)

    def check_order_window_ready(self):
        return self._wait_elem_visible(CLOSE_BUTTON_LOCATOR_OVER).is_displayed()
