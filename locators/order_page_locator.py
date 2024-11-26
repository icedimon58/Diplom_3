from selenium.webdriver.common.by import By

ORDER_NUMBER_LOCATOR = By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"

ORDER_READY_LOCATOR = By.XPATH, "//div[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"

ORDER_LOCATOR = By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6'][1]"

ORDER_TEXT_LOCATOR = By.XPATH, "//div/h2[@class='text text_type_main-medium mb-2']"

USERS_ORDER_IN_MAIN_LIST = By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']/a/div/p[@class='text text_type_digits-default']"

ORDERS_DONE_FOR_ALL_TIME = By.XPATH, "//div[@class='undefined mb-15']/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"

ORDERS_DONE_TODAY = By.XPATH, "//div[last()]/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"

ORDERS_IN_WORK = By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']"
