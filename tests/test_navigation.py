from pages.home_page import HomePage


def test_navigation(driver):
    home = HomePage(driver)
    home.open_home()

    assert driver.title != ""