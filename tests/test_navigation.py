import allure
from pages.main_page import MainPage
from config import Config

@allure.feature("Навигация")
class TestNavigation:
    @allure.title("Возврат на главную по логотипу 'Самокат'")
    def test_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button_top()
        main_page.click_scooter_logo()
        assert driver.current_url == Config.BASE_URL

    @allure.title("Переход на Дзен по логотипу 'Яндекс'")
    def test_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.switch_to_new_window()
        assert Config.DZEN_PAGE_URL in driver.current_url
        