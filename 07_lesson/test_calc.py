from selenium import webdriver
from CalculatorPage import CalculatorPage


def test_slow_calculator():
    driver = webdriver.Chrome()

    page = CalculatorPage(driver)
    page.open()

    page.set_delay("45")

    page.click_button("7")
    page.click_operator("+")
    page.click_button("8")
    page.click_equals()

    result = page.wait_for_result("15", timeout=46)
    assert result

    driver.quit()
