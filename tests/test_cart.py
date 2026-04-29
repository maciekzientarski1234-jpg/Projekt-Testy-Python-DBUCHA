from pages.home_page import HomePage
from pages.product_page import ProductPage


def test_add_to_cart(driver):
    home = HomePage(driver)
    product = ProductPage(driver)

    home.open_home()
    home.open_products()
    home.open_first_product()
    product.add_to_cart()