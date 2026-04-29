from pages.home_page import HomePage


def test_open_product(driver):
    home = HomePage(driver)

    home.open_home()
    home.open_first_product()

    assert "/products/" in driver.current_url