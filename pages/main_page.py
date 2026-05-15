from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

class MainPage(BasePage):
    def click_on_accordion_question(self, index):
        with allure.step(f"Клик по вопросу {index + 1} в разделе 'Вопросы о важном'"):
            self.click_element(MainPageLocators.ACCORDION_QUESTIONS[index])

    def get_accordion_answer_text(self, index):
        with allure.step(f"Получение текста ответа на вопрос {index + 1}"):
            return self.get_text(MainPageLocators.ACCORDION_ANSWERS[index])

    def click_order_button_top(self):
        with allure.step("Клик по кнопке 'Заказать' в хедере"):
            self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        with allure.step("Клик по кнопке 'Заказать' в футере"):
            self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_scooter_logo(self):
        with allure.step("Клик по логотипу 'Самокат'"):
            self.click_element(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        with allure.step("Клик по логотипу 'Яндекс'"):
            self.click_element(MainPageLocators.YANDEX_LOGO)