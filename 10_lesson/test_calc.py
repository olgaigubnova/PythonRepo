import allure
from allure_commons.types import Severity
from selenium import webdriver

from CalculatorPage import CalculatorPage


@allure.title("Сложение чисел в медленном калькуляторе")
@allure.description("Проверка корректности сложения 7 + 8 с задержкой вычислений")
@allure.feature("Calculator")
@allure.severity(Severity.NORMAL)
def test_slow_calculator():
    driver = webdriver.Chrome()
    page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        page.open()

    with allure.step("Установить задержку вычислений"):
        page.set_delay("45")

    with allure.step("Выполнить операцию 7 + 8"):
        page.click_button("7")
        page.click_operator("+")
        page.click_button("8")
        page.click_equals()

    with allure.step("Проверить результат вычисления"):
        result = page.wait_for_result("15", timeout=46)
        assert result is True

    driver.quit()