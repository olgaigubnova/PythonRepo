from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    wait = WebDriverWait(driver, 10)

    try:
        # Вводим задержку 45
        delay_input = wait.until(
            EC.presence_of_element_located((By.ID, "delay")))
        delay_input.clear()
        delay_input.send_keys("45")

        # Нажимаем кнопки калькулятора
        driver.find_element(
            By.XPATH,
            "//span[contains(@class, 'btn') and text()='7']"
            ).click()
        driver.find_element(
            By.XPATH,
            "//span[contains(@class, 'operator') and text()='+']"
            ).click()
        driver.find_element(
            By.XPATH,
            "//span[contains(@class, 'btn') and text()='8']"
            ).click()
        driver.find_element(
            By.XPATH,
            "//span[contains(@class, 'btn-outline-warning') and text()='=']"
            ).click()

        # Ждем, пока результат будет равен 15
        result = WebDriverWait(driver, 46).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), "15"))

        assert result

    finally:
        driver.quit()
