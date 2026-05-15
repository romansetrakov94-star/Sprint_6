from selenium.webdriver.common.by import By

class MainPageLocators:
    # Раздел "Вопросы о важном"
    ACCORDION_QUESTIONS = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7"),
    ]
    
    ACCORDION_ANSWERS = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7"),
    ]
    
    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton__1_cWm')]//button[text()='Заказать']")
    
    # Логотипы для навигации
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@href, '/') and contains(@class, 'Header_LogoScooter__3lsAR')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@href, 'dzen.ru') and contains(@class, 'Header_LogoYandex__3TSOI')]")
    