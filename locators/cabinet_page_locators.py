from selenium.webdriver.common.by import By

HISTORY_BTN = By.XPATH, "//*[text()='История заказов']"

EXIT_BTN = By.XPATH, "//*[text()='Выход']"

LOAD_TEXT = By.XPATH, "//div[@class='App_centeredComponent__tXJuB text text_type_main-large']"

USERS_ORDER_IN_HISTORY = By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6'][last()]/a/div/p[@class='text text_type_digits-default']"
