import pytest
from selenium import webdriver
from helpers import Order

@pytest.fixture(scope="class")
def driver(request):
    driver = webdriver.Firefox()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(params=[1, 2],scope="class")
def order(request, driver):
    order = Order()
    request.cls.order = order
    return order

