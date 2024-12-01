import pytest
from selenium import webdriver

from data import PAGE_URL


@pytest.fixture(params=["chrome", "firefox"])
def page_driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.get(PAGE_URL)
    yield driver
    driver.quit()
