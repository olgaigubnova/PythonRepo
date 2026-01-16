from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Класс страницы авторизации.
    """

    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы логина.

        :param driver: Экземпляр Selenium WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> None:
        """
        Открывает страницу авторизации.

        :return: None
        """
        self.driver.get(self.URL)

    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию пользователя.

        :param username: Имя пользователя
        :param password: Пароль пользователя
        :return: None
        """
        self.wait.until(
            EC.presence_of_element_located(self.USERNAME)
        ).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()