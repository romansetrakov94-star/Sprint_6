import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step("Клик по вопросу")
    def click_question(self, index: int):
        self.click(MainPageLocators.get_question_locator(index))

    @allure.step("Получение текста ответа")
    def get_answer_text(self, index: int) -> str:
        return self.get_text(MainPageLocators.get_answer_locator(index))

    @allure.step("Клик по кнопке 'Заказать' в хедере")
    def click_order_button_top(self):
        self.click(MainPageLocators.ORDER_BTN_HEADER)

    @allure.step("Клик по кнопке 'Заказать' в футере")
    def click_order_button_bottom(self):
        self.click(MainPageLocators.ORDER_BTN_FOOTER)

    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)
        