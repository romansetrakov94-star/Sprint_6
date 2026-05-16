# Sprint_6 – UI-тесты для Яндекс.Самокат

## Установка и запуск
1. Создать виртуальное окружение: `python -m venv .venv`
2. Активировать: `.\.venv\Scripts\activate` (Windows)
3. Установить зависимости: `pip install -r requirements.txt`
4. Запустить тесты: `pytest tests/ --browser=firefox --alluredir=allure_results`
5. Посмотреть отчёт: `allure serve allure_results`

## Структура
- `config/` – конфигурация
- `locators/` – локаторы элементов
- `pages/` – Page Object модели
- `tests/` – тесты
