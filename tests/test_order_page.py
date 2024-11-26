import allure

from pages.order_page import OrderPage
from data import USER_MAIL, USER_PASS, ORDER_TEXT_EXPECTED_TEXT


class TestOrderPage:

    @allure.description('Проверка того, что если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.title('Проверка всплывающего окна')
    def test_check_taking_order(self, page_driver):
        order_page = OrderPage(page_driver)
        order_page.wait_overlay_disipearing()
        order_page.redirect_to_orders()
        order_info = order_page.get_order_text()
        order_page.get_order_info()
        assert order_page.get_order_text_info() in order_info

    @allure.description('Проверка того, что авторизованный пользователь может сделать заказ')
    @allure.title('Проверка оформления заказа')
    def test_check_taking_order_window_appear(self, page_driver):
        order_page = OrderPage(page_driver)
        order_page.wait_overlay_disipearing()
        order_page.redir_to_login_page()
        order_page.fill_email_data(USER_MAIL)
        order_page.fill_password_data(USER_PASS)
        order_page.login_btn_click()
        order_page.drag_and_drop_element()
        order_page.click_take_order_button()
        assert order_page.get_order_number() != ORDER_TEXT_EXPECTED_TEXT

    @allure.description('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»,')
    @allure.title('Проверка заказа нв разных страницах')
    def test_check_order_in_list_and_history(self, page_driver):
        order_page = OrderPage(page_driver)
        order_page.wait_overlay_disipearing()
        order_page.redir_to_login_page()
        order_page.fill_email_data(USER_MAIL)
        order_page.fill_password_data(USER_PASS)
        order_page.login_btn_click()
        order_page.drag_and_drop_element()
        order_page.click_take_order_button()
        order_number = order_page.get_order_number()
        order_page.close_ingredient_window()
        order_page.redirect_to_login_page()
        order_page.click_on_history_button()
        number_in_history = order_page.find_order_in_user_history()[2:]
        order_page.redirect_to_orders()
        order_page.find_user_order_in_orders()
        assert order_number == number_in_history == order_page.find_user_order_in_orders()[2:]

    @allure.description('Проверка того, что при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    @allure.title('Проверка счетчика "Выполнено за всё время"')
    def test_check_count_for_all_time_changes_positive(self, page_driver):
        order_page = OrderPage(page_driver)
        order_page.wait_overlay_disipearing()
        order_page.redir_to_login_page()
        order_page.fill_email_data(USER_MAIL)
        order_page.fill_password_data(USER_PASS)
        order_page.login_btn_click()
        order_page.redirect_to_orders()
        orders_before = order_page.get_orders_for_all_time()
        order_page.redirect_to_condtructor()
        order_page.drag_and_drop_element()
        order_page.click_take_order_button()
        order_page.get_order_number()
        order_page.close_ingredient_window()
        order_page.redirect_to_orders()
        orders_after = order_page.get_orders_for_all_time()
        assert orders_after > orders_before

    @allure.description('Проверка того, что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    @allure.title('Проверка счетчика "Выполнено за сегодня"')
    def test_check_count_for_today_changes_positive(self, page_driver):
        order_page = OrderPage(page_driver)
        order_page.wait_overlay_disipearing()
        order_page.redir_to_login_page()
        order_page.fill_email_data(USER_MAIL)
        order_page.fill_password_data(USER_PASS)
        order_page.login_btn_click()
        order_page.redirect_to_orders()
        orders_number = order_page.get_order_number()
        order_page.redirect_to_condtructor()
        order_page.drag_and_drop_element()
        order_page.click_take_order_button()
        order_page.get_order_number()
        order_page.close_ingredient_window()
        order_page.redirect_to_orders()
        orders_after = order_page.get_orders_for_today()
        assert orders_after[2:] == orders_number

    @allure.description('Проверка того, что при создании нового заказ он появляется в поле "В работе" ')
    @allure.title('Проверка поля "В работе"')
    def test_check_count_for_today_changes_positive(self, page_driver):
        order_page = OrderPage(page_driver)
        order_page.wait_overlay_disipearing()
        order_page.redir_to_login_page()
        order_page.fill_email_data(USER_MAIL)
        order_page.fill_password_data(USER_PASS)
        order_page.login_btn_click()
        order_page.redirect_to_orders()
        order_page.redirect_to_condtructor()
        order_page.drag_and_drop_element()
        order_page.click_take_order_button()
        order_num = order_page.get_order_number()
        order_page.close_ingredient_window()
        order_page.redirect_to_orders()
        orders_after = order_page.get_orders_in_work()
        assert orders_after[1:] == order_num
