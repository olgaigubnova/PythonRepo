# UI автотесты (Selenium + PyTest + Allure)

## Описание проекта

Проект содержит UI автотесты для веб-приложений с использованием:
- Python
- Selenium WebDriver
- PyTest
- Allure Report

В проекте реализован паттерн **Page Object Model (POM)**.  
Все Page-классы задокументированы, в тестах используется Allure для формирования отчётов.

Тестируемые приложения:
- Интернет-магазин: https://www.saucedemo.com/
- Медленный калькулятор: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html

---

## Структура проекта
project/
│
├── pages/ # Page Object классы
│ ├── LoginPage.py
│ ├── MainShopPage.py
│ ├── CartPage.py
│ └── CheckoutPage.py
│
├── tests и # Page Object классы для калькулятора
│ ├── test_shop.py
  ├── CalculatorPage.py
│ └── test_calc.py
│
├── allure-results/ # Результаты тестов (не добавляются в репозиторий)
├── allure-report/ # HTML отчет Allure (не добавляется в репозиторий)
│
├── README.md
└── .gitignore