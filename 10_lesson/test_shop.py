import allure
from allure_commons.types import Severity
from selenium import webdriver

from pages.LoginPage import LoginPage
from pages.MainShopPage import MainShopPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage


@allure.title("Проверка итоговой суммы заказа")
@allure.description(
    "Проверка корректности итоговой стоимости "
    "при покупке нескольких товаров"
)
@allure.feature("Shop")
@allure.severity(Severity.CRITICAL)
def test_shop_total_price():
    driver = webdriver.Firefox()

    login_page = LoginPage(driver)
    shop_page = MainShopPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    with allure.step("Открыть страницу логина"):
        login_page.open()

    with allure.step("Авторизоваться пользователем"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        shop_page.add_backpack()
        shop_page.add_bolt_tshirt()
        shop_page.add_onesie()

    with allure.step("Перейти в корзину"):
        shop_page.go_to_cart()

    with allure.step("Перейти к оформлению заказа"):
        cart_page.checkout()

    with allure.step("Заполнить данные покупателя"):
        checkout_page.fill_form("Ivan", "Petrov", "123456")

    with allure.step("Продолжить оформление заказа"):
        checkout_page.continue_checkout()

    with allure.step("Проверить итоговую сумму заказа"):
        total = checkout_page.get_total_text()
        assert total == "Total: $58.29"

    driver.quit()
