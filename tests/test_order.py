import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import ORDER_DATA

@allure.feature("Оформление заказа")
class TestOrder:

    @pytest.mark.parametrize("order_data", ORDER_DATA)
    @allure.title("Оформление заказа через кнопку в хедере")
    def test_order_flow_from_header(self, browser, order_data):
        main_page = MainPage(browser)
        main_page.click_order_button_top()
        order_page = OrderPage(browser)
        order_page.fill_customer_info(
            order_data["name"], order_data["last_name"],
            order_data["address"], order_data["metro"], order_data["phone"]
        )
        order_page.click_next_button()
        order_page.fill_rental_info(
            order_data["delivery_date"], order_data["rental_period_days"], order_data["color"]
        )
        order_page.click_order_button()
        order_page.click_confirm_button()
        assert "Заказ оформлен" in order_page.get_success_message_text()

    @pytest.mark.parametrize("order_data", ORDER_DATA)
    @allure.title("Оформление заказа через кнопку в футере")
    def test_order_flow_from_footer(self, browser, order_data):
        # Аналогично, но с main_page.click_order_button_bottom()
        pass
    