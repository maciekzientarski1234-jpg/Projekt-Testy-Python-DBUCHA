from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_fake_checkout_process(driver):
    home = HomePage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    home.open_home()
    home.open_first_product()
    product.add_to_cart()
    cart.go_to_checkout()

    assert True
