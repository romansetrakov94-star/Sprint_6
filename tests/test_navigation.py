import allure
from config import BASE_URL, YANDEX_URL
from pages.main_page import MainPage

@allure.feature("Навигация")
class TestNavigation:

    @allure.title("Переход на главную по клику на логотип 'Самокат'")
    def test_scooter_logo_redirect(self, browser):
        browser.get(BASE_URL)
        main_page = MainPage(browser)
        main_page.click_scooter_logo()
        assert browser.current_url == BASE_URL

    @allure.title("Переход на Яндекс.Дзен по клику на логотип 'Яндекс'")
    def test_yandex_logo_redirect(self, browser):
        browser.get(BASE_URL)
        main_page = MainPage(browser)
        main_page.click_yandex_logo()
        browser.switch_to.window(browser.window_handles[-1])
        assert YANDEX_URL in browser.current_url
        