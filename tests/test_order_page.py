import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LocatorsOrderPage
from page_objects.order_page import OrderPageScooter
from data import Url
from helpers import Order


@pytest.mark.usefixtures('driver')
class TestOrderPage:

    @allure.title('Проверка оформления заказа')
    @pytest.mark.parametrize('button_locator',
                             [LocatorsOrderPage.order_button_up, LocatorsOrderPage.order_button_down])
    def test_order_creation(self, driver, button_locator):

        test_order = Order()
        order_page = OrderPageScooter(driver)

        is_created = order_page.make_order(
            name=test_order.name,
            surname=test_order.surname,
            address=test_order.address,
            station=test_order.station,
            telephone=test_order.telephone,
            date=test_order.date,
            rental_period=test_order.rental_period,
            color=test_order.color,
            comment=test_order.comment,
            locator=button_locator
        )

        assert is_created, "Окно подтверждения заказа не отобразилось"

    @allure.title('Проверка перехода на главную через логотип Самоката')
    def test_navigation_via_scooter_logo(self, driver):
        order_page = OrderPageScooter(driver)
        order_page.go_to_site()
        order_page.go_from_logo_samokat_to_home_page()

        assert order_page.driver_current_url() == Url.url_home_page, (
            f"Ожидался {Url.url_home_page}, получен {order_page.driver_current_url()}"
        )

    @allure.title('Проверка перехода в Дзен через логотип Яндекса')
    def test_check_from_logo_yandex_to_dzen(self, driver):
        order_page = OrderPageScooter(driver)
        order_page.go_to_site()

        order_page.go_from_logo_yandex_to_dzen()

        WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in driver.current_url, (
            f"Ожидался URL содержащий 'dzen.ru', получен {driver.current_url}"
        )