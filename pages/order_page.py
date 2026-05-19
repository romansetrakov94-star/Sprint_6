from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure

class OrderPage(BasePage):
    @allure.step("Заполнение информации о клиенте")
    def fill_customer_info(self, name, last_name, address, metro, phone):
        self.send_keys(OrderPageLocators.NAME_FIELD, name)
        self.send_keys(OrderPageLocators.LAST_NAME_FIELD, last_name)
        self.send_keys(OrderPageLocators.ADDRESS_FIELD, address)
        self.click(OrderPageLocators.METRO_FIELD)
        self.send_keys(OrderPageLocators.METRO_FIELD, metro)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{metro}']"))).click()
        self.send_keys(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step("Клик по кнопке 'Далее'")
    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнение информации об аренде")
    def fill_rental_info(self, delivery_date, rental_period, color):
        # Дата
        date_field = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.DATE_FIELD))
        date_field.click()
        date_field.clear()
        date_field.send_keys(delivery_date)
        self.press_escape()

        # Срок аренды
        dropdown = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_DROPDOWN))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
        dropdown.click()
        # Ждём появления нужной опции
        option_locator = (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and contains(text(), '{rental_period}')]")
        option = self.wait.until(EC.element_to_be_clickable(option_locator))
        self.driver.execute_script("arguments[0].click();", option)

        # Цвет
        if color.lower() == "black":
            self.click(OrderPageLocators.COLOR_BLACK)
        else:
            self.click(OrderPageLocators.COLOR_GREY)

    @allure.step("Клик по кнопке 'Заказать'")
    def click_order_button(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Получение сообщения об успешном заказе")
    def get_success_message(self):
        return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)
    