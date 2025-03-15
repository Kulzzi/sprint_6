import allure
from selenium.webdriver.common.by import By
from locators import LocatorsOrderPage
from page_objects.base_page import BasePageScooter


class OrderPageScooter(BasePageScooter):

    def __init__(self, driver, order):
        super().__init__(driver)
        self.order = order
    #не очень понимаю что от меня требуется

    @allure.step('Ввод имени')
    def set_name(self):
        element = self.driver_find_element(LocatorsOrderPage.name_field)
        self.driver_send_keys_to_element(element, self.order.name)

    @allure.step('Ввод фамилии')
    def set_surname(self):
        element = self.driver_find_element(LocatorsOrderPage.surname_field)
        self.driver_send_keys_to_element(element, self.order.surname)

    @allure.step('Ввод адреса доставки')
    def set_address(self):
        element = self.driver_find_element(LocatorsOrderPage.address_field)
        self.driver_send_keys_to_element(element, self.order.address)

    @allure.step('Выбор станции метро')
    def choose_station(self):
        element = self.driver_find_element(LocatorsOrderPage.station_field_1)
        self.driver_wait_for_clickable_element(LocatorsOrderPage.station_field_1)
        self.driver_click_element(element)
        element = self.driver_find_element(LocatorsOrderPage.station_field_2)
        self.driver_send_keys_to_element(element, self.order.station)
        elements = self.driver_find_elements(LocatorsOrderPage.station_field_3)

        for element in elements:
            if element.text == self.order.station:
                self.driver_scroll_to_element(element)
                self.driver_click_element(element)
                break

    @allure.step('Ввод номера телефона')
    def set_telephone(self):
        element = self.driver_find_element(LocatorsOrderPage.telephone_field)
        self.driver_send_keys_to_element(element, self.order.telephone)

    @allure.step('Нажатие на кнопку "Далее"')
    def click_sign_in_button(self):
        element = self.driver_find_element(LocatorsOrderPage.order_button_next)
        self.driver_click_element(element)

    @allure.step('Выбор даты доставки')
    def set_date(self):
        element = self.driver_find_element(LocatorsOrderPage.date_field)
        self.driver_click_element(element)
        element = self.driver_find_element(LocatorsOrderPage.current_day)
        day_str = str(int(element.text) + self.order.date)
        element = self.driver_find_element([By.XPATH, f".//div[text()={day_str}]"])
        self.driver_click_element(element)

    @allure.step('Выбор периода аренды')
    def choose_rental_period(self):
        element = self.driver_find_element(LocatorsOrderPage.rental_period_field)
        self.driver_click_element(element)
        element = self.driver_find_element([By.XPATH, f".//div[text()='{self.order.rental_period}']"])
        self.driver_click_element(element)

    @allure.step('Выбор цвета')
    def choose_color(self):
        element = self.driver_find_element(LocatorsOrderPage.color_field)
        self.driver_click_element(element)
        element = self.driver_find_element([By.ID, f"{self.order.color}"])
        self.driver_click_element(element)

    @allure.step('Ввод комментария к заказу')
    def set_comment(self):
        element = self.driver_find_element(LocatorsOrderPage.comment_field)
        self.driver_send_keys_to_element(element, self.order.comment)

    @allure.step('Нажатие кнопки "Заказать"')
    def click_sign_in_button2(self):
        element = self.driver_find_elements(LocatorsOrderPage.order_button_final)[1]
        self.driver_click_element(element)

    @allure.step('Создание заказа')
    def make_order(self, locator=LocatorsOrderPage.order_button_up):
        self.go_to_site()
        element = self.driver_find_element(locator)
        self.driver_scroll_to_element(element)
        self.driver_wait_for_clickable_element(locator)
        self.driver_click_element(element)
        self.driver_wait_for_visibile_element(LocatorsOrderPage.order_header)
        self.set_name()
        self.set_surname()
        self.set_address()
        self.choose_station()
        self.set_telephone()
        self.click_sign_in_button()
        self.driver_wait_for_visibile_element(LocatorsOrderPage.order_header)
        self.set_date()
        self.choose_rental_period()
        self.choose_color()
        self.set_comment()
        self.click_sign_in_button2()
        self.driver_wait_for_visibile_element(LocatorsOrderPage.pop_up_window)

        if self.driver_find_element(LocatorsOrderPage.pop_up_window):
            return True

    @allure.step('Переход на основную страницу по нажатию на логотип "Самокат"')
    def go_from_logo_samokat_to_home_page(self):
        element = self.driver_find_element(LocatorsOrderPage.order_button_not)
        self.driver_click_element(element)
        element = self.driver_find_element(LocatorsOrderPage.logo_scooter)
        self.driver_click_element(element)
        self.driver_wait_for_visibile_element(LocatorsOrderPage.logo_scooter)

    @allure.step('Переход на страницу Дзен по нажатию на логотип "Яндекс"')
    def go_from_logo_yandex_to_dzen(self):
        element = self.driver_find_element(LocatorsOrderPage.order_button_not)
        self.driver_click_element(element)
        element = self.driver_find_element(LocatorsOrderPage.logo_yandex)
        self.driver_click_element(element)

        self.driver_switch_to_window()
        self.driver_wait_for_visibile_element(LocatorsOrderPage.logo_dzen)