from selenium.webdriver.common.by import By

RESTORE_PASS_EMAIL_FIELD = By.XPATH, "//input[@class='text input__textfield text_type_main-default']"

RESTORE_PASS_PAGE_TEXT = By.XPATH, "//*[text()='Восстановление пароля']"

RESTORE_BTN = By.XPATH, "//*[text()='Восстановить']"

RESTORE_PSWD_LINK = By.XPATH, "//a[@href='/forgot-password']"
