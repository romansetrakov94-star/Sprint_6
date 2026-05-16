from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click(self, locator):
        with allure.step(f"Клик по элементу {locator}"):
            element = self.wait.until(EC.element_to_be_clickable(locator))
            # Скроллим к элементу (на всякий случай)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            # Кликаем через JavaScript, чтобы избежать перекрытия
            self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text):
        with allure.step(f"Ввод текста '{text}' в поле {locator}"):
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)

    def get_text(self, locator):
        with allure.step(f"Получение текста из элемента {locator}"):
            return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_element_displayed(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False

    def switch_to_new_window(self):
        # Ждём появления второго окна
        self.wait.until(lambda d: len(d.window_handles) > 1)
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)
        # Ждём, пока URL перестанет быть about:blank
        self.wait.until(lambda d: d.current_url != "about:blank")
        