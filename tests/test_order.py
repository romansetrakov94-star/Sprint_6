import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.feature("Оформление заказа")
class TestOrder:
    @allure.title("Оформление заказа")
    @pytest.mark.parametrize("button_type, data", [
        ("header", {"name": "Луи", "last_name": "Луев", "address": "ул. Пушкина, д. 10",
                    "metro": "Сокольники", "phone": "79991234567",
                    "delivery_date": "15.12.2025", "rental_period": "сутки", "color": "black"}),
        ("footer", {"name": "Луиза", "last_name": "Луизова", "address": "ул. Лермонтова, д. 15",
                    "metro": "Преображенская площадь", "phone": "79261234567",
                    "delivery_date": "20.12.2025", "rental_period": "двое суток", "color": "grey"})
    ])
    def test_order(self, driver, button_type, data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        if button_type == "header":
            main_page.click_order_button_top()
        else:
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
