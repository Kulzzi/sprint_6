import allure
import pytest
from data import Answers
from locators import LocatorsHomePage
from page_objects.home_page import HomePageScooter


@pytest.mark.usefixtures('driver')
class TestHomePage:

    @allure.title('Проверка текста ответа на вопрос')
    @pytest.mark.parametrize('question_locator, answer_locator, answer_text',
                             [[question_locator, answer_locator, answer_text]
                              for question_locator, answer_locator, answer_text
                              in zip(LocatorsHomePage.questions, LocatorsHomePage.answers, Answers.answers)])
    def test_check_answer_on_question(self, question_locator, answer_locator, answer_text):
        question_answer = HomePageScooter(self.driver)
        question_answer.go_to_site()
        answer_on_question = question_answer.answer_on_question(question_locator, answer_locator)

        assert answer_on_question == answer_text