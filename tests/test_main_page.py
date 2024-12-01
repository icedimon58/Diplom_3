import allure

from data import INGRIDIENTS_EXPECTED_TEXT
from pages.main_page import MainPage
from pages.general_methods import GeneralMethodsPage


class TestMainPage:

    @allure.description('При выборе ингредиента должно появиться окно с его информацией')
    @allure.title('Проверка окна информации по ингредиенту')
    def test_click_on_ingredient(self, page_driver):
        main_page = MainPage(page_driver)
        general_methods = GeneralMethodsPage(page_driver)
        general_methods.wait_overlay_disipearing()
        main_page.click_on_get_ingridient()
        assert main_page.get_ingredient_window_text() == INGRIDIENTS_EXPECTED_TEXT

    @allure.description('Проверка закрытия окна информации об ингредиенте по клику на крестик')
    @allure.title('Проверка закрытия окна ')
    def test_click_on_ingredient_cross(self, page_driver):
        main_page = MainPage(page_driver)
        general_methods = GeneralMethodsPage(page_driver)
        general_methods.wait_overlay_disipearing()
        main_page.click_on_get_ingridient()
        main_page.close_ingredient_window()
        assert main_page.check_close_btn_invisible()

    @allure.description('Проверка того, что при перетаскивании изменится счетчик у ингредиента')
    @allure.title('Проверка перетаскивания ингредиентов')
    def test_drag_and_drop_test(self, page_driver):
        main_page = MainPage(page_driver)
        main_page.drag_and_drop_element()
        assert main_page.check_drag_and_drop()
