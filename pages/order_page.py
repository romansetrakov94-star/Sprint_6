from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure

class OrderPage(BasePage):
    def fill_customer_info(self, name, last_name, address, metro, phone):
        with allure.step(f"Заполнение информации о клиенте: {name} {last_name}"):
            self.send_keys(OrderPageLocators.NAME_FIELD, name)
            self.send_keys(OrderPageLocators.LAST_NAME_FIELD, last_name)
            self.send_keys(OrderPageLocators.ADDRESS_FIELD, address)
            self.click_element(OrderPageLocators.METRO_FIELD)
            self.send_keys(OrderPageLocators.METRO_FIELD, metro)
            self.click_element((By.XPATH, f"//div[text()='{metro}']"))
            self.send_keys(OrderPageLocators.PHONE_FIELD, phone)

    def click_next_button(self):
        with allure.step("Клик по кнопке 'Далее'"):
            self.click_element(OrderPageLocators.NEXT_BUTTON)

    def fill_rental_info(self, delivery_date, rental_period_days, color):
        with allure.step(f"Заполнение информации об аренде: до {delivery_date}, на {rental_period_days} суток"):
            self.send_keys(OrderPageLocators.DELIVERY_DATE_FIELD, delivery_date)
            self.click_element(OrderPageLocators.RENTAL_PERIOD)
            options = self.driver.find_elements(*OrderPageLocators.RENTAL_OPTIONS)
            for option in options:
                if rental_period_days in option.text:
                    option.click()
                    break
            if color == "black":
                self.click_element(OrderPageLocators.COLOR_BLACK)
            elif color == "grey":
                self.click_element(OrderPageLocators.COLOR_GREY)

    def click_order_button(self):
        with allure.step("Клик по кнопке 'Заказать'"):
            self.click_element(OrderPageLocators.ORDER_BUTTON)

    def click_confirm_button(self):
        with allure.step("Подтверждение заказа"):
            self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    def get_success_message_text(self):
        with allure.step("Получение текста сообщения об успешном заказе"):
            return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)
        