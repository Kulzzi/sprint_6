import allure
from page_objects.base_page import BasePageScooter


class HomePageScooter(BasePageScooter):

    def answer_on_question(self, question_locator, answer_locator):
        element = self.driver_find_element(question_locator)
        self.driver_scroll_to_element(element)
        self.driver_wait_for_clickable_element(question_locator)
        self.driver_click_element(element)
        self.driver_wait_for_visibile_element(answer_locator)

        return self.driver_find_element(answer_locator).text