from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Клик по элементу")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввод текста в поле")
    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста элемента")
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Проверка отображения элемента")
    def is_element_displayed(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False

    @allure.step("Переключение на новое окно")
    def switch_to_new_window(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)
        self.wait.until(lambda d: d.current_url != "about:blank")

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Нажатие клавиши Escape")
    def press_escape(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        