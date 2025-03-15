from selenium.webdriver.common.by import By


class LocatorsHomePage:

    list_subheader = [By.CLASS_NAME, 'Home_SubHeader__zwi_E']

    questions = [
                [By.ID, "accordion__heading-0"],
                [By.ID, "accordion__heading-1"],
                [By.ID, "accordion__heading-2"],
                [By.ID, "accordion__heading-3"],
                [By.ID, "accordion__heading-4"],
                [By.ID, "accordion__heading-5"],
                [By.ID, "accordion__heading-6"],
                [By.ID, "accordion__heading-7"]
                ]

    answers = [
                [By.ID, "accordion__panel-0"],
                [By.ID, "accordion__panel-1"],
                [By.ID, "accordion__panel-2"],
                [By.ID, "accordion__panel-3"],
                [By.ID, "accordion__panel-4"],
                [By.ID, "accordion__panel-5"],
                [By.ID, "accordion__panel-6"],
                [By.ID, "accordion__panel-7"]
                ]


class LocatorsOrderPage:

    order_button_up = [By.XPATH, ".//button[@class='Button_Button__ra12g']"]
    order_button_down = [By.XPATH, ".//button/parent::div[@class='Home_FinishButton__1_cWm']"]
    order_header = [By.CLASS_NAME, "Order_Header__BZXOb"]

    name_field = [By.XPATH, ".//*[@placeholder='* Имя']"]
    surname_field = [By.XPATH, ".//*[@placeholder='* Фамилия']"]

    address_field = [By.XPATH, ".//*[@placeholder='* Адрес: куда привезти заказ']"]

    station_field_1 = [By.CLASS_NAME, "select-search__value"]
    station_field_2 = [By.CLASS_NAME, "select-search__input"]
    station_field_3 = [By.CLASS_NAME, "select-search__select"]

    order_button_next = [By.XPATH, ".//button[text()='Далее']"]

    telephone_field = [By.XPATH, ".//*[@placeholder='* Телефон: на него позвонит курьер']"]

    date_field = [By.CLASS_NAME, "react-datepicker__input-container"]
    current_day = [By.XPATH, ".//div[contains(@class, 'today')]"]

    rental_period_field = [By.XPATH, ".//*[@class='Dropdown-placeholder']"]

    color_field = [By.XPATH, ".//*[@class='Order_Checkboxes__3lWSI']"]

    comment_field = [By.XPATH, ".//*[@placeholder='Комментарий для курьера']"]

    order_button_final = [By.XPATH, ".//button[text()='Заказать']"]

    pop_up_window = [By.CLASS_NAME, "Order_Modal__YZ-d3"]

    order_button_not = [By.XPATH, ".//button[text()='Нет']"]
    logo_scooter = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]
    logo_yandex = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]

    logo_dzen = [By.XPATH, ".//a[@data-testid='logo']"]