import allure
import pytest
from locators import LocatorsOrderPage
from page_objects.order_page import OrderPageScooter
from data import Url


@pytest.mark.usefixtures('driver', 'order')
class TestOrderPage:

    @allure.title('Проверка функции оформления заказа')
    @pytest.mark.parametrize('locator', [LocatorsOrderPage.order_button_up, LocatorsOrderPage.order_button_down])
    def test_check_order(self, locator):
        order_page = OrderPageScooter(self.driver, self.order)

        assert order_page.make_order(locator) == True

    @allure.title('Проверка перехода на главную страницу при клике на логотип сайта')
    def test_check_from_logo_samokat_to_home_page(self):
        order_page = OrderPageScooter(self.driver, self.order)
        order_page.make_order()
        order_page.go_from_logo_samokat_to_home_page()

        assert order_page.driver_current_url() == Url.url_home_page

    @allure.title('Проверка перехода на главную страницу Дзена при клике на логотип "Яндекса"')
    def test_check_from_logo_yandex_to_dzen(self):
        order_page = OrderPageScooter(self.driver, self.order)
        order_page.make_order()
        order_page.go_from_logo_yandex_to_dzen()

        assert order_page.driver_current_url() == Url.url_dzen