from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Класс страницы медленного калькулятора.
    """

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        :param driver: Экземпляр Selenium WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> None:
        """
        Открывает страницу калькулятора.

        :return: None
        """
        self.driver.get(self.URL)

    def set_delay(self, value: str) -> None:
        """
        Устанавливает задержку вычислений.

        :param value: Значение задержки в секундах
        :return: None
        """
        delay = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT)
        )
        delay.clear()
        delay.send_keys(value)

    def click_button(self, text: str) -> None:
        """
        Нажимает цифровую кнопку.

        :param text: Текст кнопки
        :return: None
        """
        button = self.driver.find_element(
            By.XPATH,
            f"//span[contains(@class, 'btn') and text()='{text}']"
        )
        button.click()

    def click_operator(self, operator: str) -> None:
        """
        Нажимает кнопку оператора.

        :param operator: Арифметический оператор
        :return: None
        """
        button = self.driver.find_element(
            By.XPATH,
            f"//span[contains(@class, 'operator') and text()='{operator}']"
        )
        button.click()

    def click_equals(self) -> None:
        """
        Нажимает кнопку '='.

        :return: None
        """
        button = self.driver.find_element(
            By.XPATH,
            "//span[contains(@class, 'btn-outline-warning') and text()='=']"
        )
        button.click()

    def wait_for_result(self, expected_text: str, timeout: int) -> bool:
        """
        Ожидает появления результата вычислений.

        :param expected_text: Ожидаемый результат
        :param timeout: Таймаут ожидания
        :return: True, если результат появился
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_text)
        )
