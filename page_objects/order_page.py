import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import LocatorsOrderPage
from page_objects.base_page import BasePageScooter


class OrderPageScooter(BasePageScooter):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Создание заказа')
    def make_order(
            self,
            name: str,
            surname: str,
            address: str,
            station: str,
            telephone: str,
            date: int,
            rental_period: str,
            color: str,
            comment: str,
            locator: tuple = LocatorsOrderPage.order_button_up
    ) -> bool:
        self.start_order_process(locator)

        self.fill_personal_info(name, surname, address, station, telephone)
        self.fill_delivery_info(date, rental_period, color, comment)

        return self.is_order_confirmed()

    def start_order_process(self, locator: tuple):
        self.go_to_site()
        element = self.driver_find_element(locator)
        self.driver_scroll_to_element(element)
        self.driver_wait_for_clickable_element(locator)
        self.driver_click_element(element)
        self.driver_wait_for_visibile_element(LocatorsOrderPage.order_header)

    def fill_personal_info(
            self,
            name: str,
            surname: str,
            address: str,
            station: str,
            telephone: str
    ):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.choose_station(station)
        self.set_telephone(telephone)
        self.click_next_button()

    def fill_delivery_info(
            self,
            date: int,
            rental_period: str,
            color: str,
            comment: str
    ):
        self.set_date(date)
        self.choose_rental_period(rental_period)
        self.choose_color(color)
        self.set_comment(comment)
        self.click_final_order_button()

    @allure.step('Ввод имени')
    def set_name(self, name: str):
        element = self.driver_find_element(LocatorsOrderPage.name_field)
        self.driver_send_keys_to_element(element, name)

    @allure.step('Ввод фамилии')
    def set_surname(self, surname: str):
        element = self.driver_find_element(LocatorsOrderPage.surname_field)
        self.driver_send_keys_to_element(element, surname)

    @allure.step('Ввод адреса')
    def set_address(self, address: str):
        element = self.driver_find_element(LocatorsOrderPage.address_field)
        self.driver_send_keys_to_element(element, address)

    @allure.step('Выбор станции метро')
    def choose_station(self, station: str):
        self.driver_click_element(self.driver_find_element(LocatorsOrderPage.station_field_1))
        self.driver_send_keys_to_element(
            self.driver_find_element(LocatorsOrderPage.station_field_2),
            station
        )
        for element in self.driver_find_elements(LocatorsOrderPage.station_field_3):
            if element.text == station:
                self.driver_click_element(element)
                break

    @allure.step('Ввод телефона')
    def set_telephone(self, telephone: str):
        element = self.driver_find_element(LocatorsOrderPage.telephone_field)
        self.driver_send_keys_to_element(element, str(telephone))

    @allure.step('Нажатие кнопки "Далее"')
    def click_next_button(self):
        self.driver_click_element(self.driver_find_element(LocatorsOrderPage.order_button_next))

    @allure.step('Выбор даты доставки')
    def set_date(self, days_offset: int):
        self.driver_click_element(self.driver_find_element(LocatorsOrderPage.date_field))
        current_day = int(self.driver_find_element(LocatorsOrderPage.current_day).text)
        target_day = current_day + days_offset
        date_element = self.driver_find_element((By.XPATH, f"//div[text()='{target_day}']"))
        self.driver_click_element(date_element)

    @allure.step('Выбор срока аренды')
    def choose_rental_period(self, period: str):
        self.driver_click_element(self.driver_find_element(LocatorsOrderPage.rental_period_field))
        period_element = self.driver_find_element((By.XPATH, f"//div[text()='{period}']"))
        self.driver_click_element(period_element)

    @allure.step('Выбор цвета самоката')
    def choose_color(self, color: str):
        element = self.driver_find_element((By.ID, color))
        self.driver_click_element((element))

    @allure.step('Ввод комментария')
    def set_comment(self, comment: str):
        element = self.driver_find_element(LocatorsOrderPage.comment_field)
        self.driver_send_keys_to_element(element, comment)

    @allure.step('Подтверждение заказа')
    def click_final_order_button(self):
        self.driver_click_element(self.driver_find_elements(LocatorsOrderPage.order_button_final)[1])

    @allure.step('Проверка подтверждения')
    def is_order_confirmed(self) -> bool:
        try:
            return bool(self.driver_find_element(LocatorsOrderPage.pop_up_window))
        except:
            return False

    # Методы навигации (оставлены без изменений)
    @allure.step('Переход на главную через логотип Самоката')
    def go_from_logo_samokat_to_home_page(self):
        self.driver_click_element(self.driver_find_element(LocatorsOrderPage.logo_scooter))

    @allure.step('Переход в Дзен через логотип Яндекса')
    def go_from_logo_yandex_to_dzen(self):
        main_window = self.driver.current_window_handle

        self.driver_click_element(self.driver_find_element(LocatorsOrderPage.logo_yandex))

        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)

        new_window = [w for w in self.driver.window_handles if w != main_window][0]
        self.driver.switch_to.window(new_window)