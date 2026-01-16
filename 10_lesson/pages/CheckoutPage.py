from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Класс страницы оформления заказа.
    """

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления заказа.

        :param driver: Экземпляр Selenium WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму оформления заказа.

        :param first_name: Имя покупателя
        :param last_name: Фамилия покупателя
        :param postal_code: Почтовый индекс
        :return: None
        """
        self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME)
        ).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    def continue_checkout(self) -> None:
        """
        Нажимает кнопку Continue для продолжения оформления заказа.

        :return: None
        """
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total_text(self) -> str:
        """
        Возвращает итоговую сумму заказа.

        :return: Текст с итоговой суммой
        """
        return self.wait.until(
            EC.presence_of_element_located(self.TOTAL_LABEL)
        ).text