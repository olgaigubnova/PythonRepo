from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Класс страницы корзины.
    Содержит методы для взаимодействия с корзиной товаров.
    """

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины.

        :param driver: Экземпляр Selenium WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout(self) -> None:
        """
        Нажимает кнопку Checkout для перехода
        к оформлению заказа.

        :return: None
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()