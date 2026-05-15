import allure
import pytest
from pages.main_page import MainPage
from data import FAQ_DATA

@allure.feature("Раздел «Вопросы о важном»")
class TestFAQ:

    @pytest.mark.parametrize("question, expected_answer", FAQ_DATA)
    @allure.title("Проверка открытия ответа на вопрос {question}")
    def test_accordion_answers(self, browser, question, expected_answer):
        main_page = MainPage(browser)
        main_page.click_on_accordion_question(question)
        answer_text = main_page.get_accordion_answer_text(question)
        assert expected_answer in answer_text, f"Ожидалось: {expected_answer}, Получено: {answer_text}"
        