import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure

class OrderPage(BasePage):
    def fill_customer_info(self, name, last_name, address, metro, phone):
        with allure.step(f"Заполнение информации о клиенте: {name} {last_name}"):
            self.send_keys(OrderPageLocators.NAME_FIELD, name)
            self.send_keys(OrderPageLocators.LAST_NAME_FIELD, last_name)
            self.send_keys(OrderPageLocators.ADDRESS_FIELD, address)
            # Кликаем по полю метро и вводим название
            self.click(OrderPageLocators.METRO_FIELD)
            self.send_keys(OrderPageLocators.METRO_FIELD, metro)
            # Ждём появления нужной станции и выбираем её
            self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{metro}']"))).click()
            self.send_keys(OrderPageLocators.PHONE_FIELD, phone)

    def click_next(self):
        with allure.step("Клик по кнопке 'Далее'"):
            self.click(OrderPageLocators.NEXT_BUTTON)

    def fill_rental_info(self, delivery_date, rental_period, color):
        with allure.step(f"Заполнение информации об аренде: до {delivery_date}, на {rental_period}"):
            # Дата
            date_field = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.DATE_FIELD))
            date_field.click()
            date_field.clear()
            date_field.send_keys(delivery_date)
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(0.5)

            # Срок аренды
            # Скроллим к дропдауну и кликаем по нему
            dropdown = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_DROPDOWN))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
            dropdown.click()
            time.sleep(0.3)  # ждём анимацию

            # Ищем конкретную опцию по тексту и кликаем
            option_locator = (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and contains(text(), '{rental_period}')]")
            option = self.wait.until(EC.element_to_be_clickable(option_locator))
            self.driver.execute_script("arguments[0].click();", option)

            # Цвет
            if color.lower() == "black":
                self.click(OrderPageLocators.COLOR_BLACK)
            else:
                self.click(OrderPageLocators.COLOR_GREY)

    def click_order_button(self):
        with allure.step("Клик по кнопке 'Заказать'"):
            self.click(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        with allure.step("Подтверждение заказа"):
            self.click(OrderPageLocators.CONFIRM_BUTTON)

    def get_success_message(self):
        with allure.step("Получение сообщения об успешном заказе"):
            return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)
        