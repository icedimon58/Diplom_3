from selenium.webdriver.common.by import By

ORDER_LINE_TEXT = By.XPATH, "//*[text()='Лента заказов']"

CONSTRUCT_LINE_TEXT = By.XPATH, "//*[text()='Соберите бургер']"

ITEM_LOCATOR = By.XPATH, "//*[text()='Краторная булка N-200i']"

ITEM_TEXT = By.XPATH, "//*[text()='Детали ингредиента']"

CLOSE_BUTTON_LOCATOR_MAIN_PAGE = By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"

CLOSE_BUTTON_LOCATOR_OVER = By.XPATH, "//div[@class='Modal_modal_overlay__x2ZCr']"

BASCET_LOCATOR = By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']"

INGRIDIENT_LOCATOR = By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6c']/div/p[contains(@class,'counter_counter__num__3nue1')]"

TAKE_ORDER_LOCATOR = By.XPATH, "//*[text()='Оформить заказ']"
