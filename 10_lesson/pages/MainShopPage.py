from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainShopPage:
    """
    Класс главной страницы магазина.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация главной страницы магазина.

        :param driver: Экземпляр Selenium WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack(self) -> None:
        """
        Добавляет товар Sauce Labs Backpack в корзину.

        :return: None
        """
        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        ).click()

    def add_bolt_tshirt(self) -> None:
        """
        Добавляет товар Bolt T-Shirt в корзину.

        :return: None
        """
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()

    def add_onesie(self) -> None:
        """
        Добавляет товар Onesie в корзину.

        :return: None
        """
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        ).click()

    def go_to_cart(self) -> None:
        """
        Переходит в корзину товаров.

        :return: None
        """
        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        ).click()