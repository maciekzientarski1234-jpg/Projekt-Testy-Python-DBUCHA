from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage


def test_go_to_checkout(driver):
    home = HomePage(driver)
    product = ProductPage(driver)
    checkout = CheckoutPage(driver)

    home.open_home()
    home.open_first_product()

    product.add_to_cart()
    product.go_to_checkout_popup()

    checkout.fill_fake_data()