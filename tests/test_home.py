from pages.home_page import HomePage


def test_homepage_load(driver):
    home = HomePage(driver)
    home.open_home()

    assert "dbucha" in driver.current_url