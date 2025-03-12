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


@pytest.fixture(params=["data1", "data2"],scope="class")
def order(request, driver):
    if request.param == "data1":
        order = Order()
    if request.param == "data2":
        order = Order()

    request.cls.order = order