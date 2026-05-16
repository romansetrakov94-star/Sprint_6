import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.feature("Оформление заказа")
class TestOrder:
    @allure.title("Оформление заказа через верхнюю кнопку")
    @pytest.mark.parametrize("data", [
        {"name": "Иван", "last_name": "Иванов", "address": "ул. Пушкина, д. 10",
         "metro": "Сокольники", "phone": "79991234567",
         "delivery_date": "15.12.2025", "rental_period": "сутки", "color": "black"},
        {"name": "Петр", "last_name": "Петров", "address": "пр. Ленина, д. 5",
         "metro": "Черкизовская", "phone": "79123456789",
         "delivery_date": "16.12.2025", "rental_period": "трое суток", "color": "grey"}
    ])
    def test_order_from_header(self, driver, data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_order_button_top()
        order_page.fill_customer_info(
            data["name"], data["last_name"],
            data["address"], data["metro"], data["phone"]
        )
        order_page.click_next()
        order_page.fill_rental_info(
            data["delivery_date"], data["rental_period"], data["color"]
        )
        order_page.click_order_button()
        order_page.confirm_order()
        assert "Заказ оформлен" in order_page.get_success_message()

    @allure.title("Оформление заказа через нижнюю кнопку")
    @pytest.mark.parametrize("data", [
        {"name": "Мария", "last_name": "Сидорова", "address": "ул. Лермонтова, д. 15",
         "metro": "Преображенская площадь", "phone": "79261234567",
         "delivery_date": "20.12.2025", "rental_period": "двое суток", "color": "grey"}
    ])
    def test_order_from_footer(self, driver, data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_order_button_bottom()
        order_page.fill_customer_info(
            data["name"], data["last_name"],
            data["address"], data["metro"], data["phone"]
        )
        order_page.click_next()
        order_page.fill_rental_info(
            data["delivery_date"], data["rental_period"], data["color"]
        )
        order_page.click_order_button()
        order_page.confirm_order()
        assert "Заказ оформлен" in order_page.get_success_message()
        