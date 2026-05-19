from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BTN_HEADER = (By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']")
    ORDER_BTN_FOOTER = (By.XPATH, "//div[contains(@class, 'Home')]//button[text()='Заказать']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    
    @staticmethod
    def get_question_locator(index: int):
        return (By.ID, f"accordion__heading-{index}")
    
    @staticmethod
    def get_answer_locator(index: int):
        return (By.ID, f"accordion__panel-{index}")
    