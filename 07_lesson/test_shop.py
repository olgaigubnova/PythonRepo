from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.MainShopPage import MainShopPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage


def test_shop_total_price():
    driver = webdriver.Firefox()

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    shop_page = MainShopPage(driver)
    shop_page.add_backpack()
    shop_page.add_bolt_tshirt()
    shop_page.add_onesie()
    shop_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Ivan", "Petrov", "123456")
    checkout_page.continue_checkout()

    total = checkout_page.get_total_text()
    assert total == "Total: $58.29"

    driver.quit()
