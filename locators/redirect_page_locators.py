from selenium.webdriver.common.by import By

OVERLAY_LOAD_LOCATOR_REDIR_PAGE = By.XPATH, "//div/div[@class='Modal_modal_overlay__x2ZCr']"

ORDER_LINE_TEXT_REDIR_PAGE = By.XPATH, "//*[text()='Лента заказов']"

CONSTRUCT_LINE_TEXT_REDIR_PAGE = By.XPATH, "//*[text()='Соберите бургер']"

KABINET_LOCATOR = By.XPATH, "//header/nav/a/p"

ORDERS_LINE = By.XPATH, "//a[@href='/feed']"

CONSTRUCT_LINE_BTN = By.XPATH, "//*[text()='Конструктор']"

ORDERS_LINE_HEADER = By.XPATH, "//a[@href='/feed']"

USER_ORDER_IN_ORDERS_LIST = By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6'][last()]/a/div/p[@class='text text_type_digits-default']'"
