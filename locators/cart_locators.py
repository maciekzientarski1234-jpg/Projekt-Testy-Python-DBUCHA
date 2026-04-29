from selenium.webdriver.common.by import By

class CartLocators:
    CART_ITEMS = (By.CSS_SELECTOR, "a.cart-item__name")
    CART_ICON = (By.CSS_SELECTOR, "a[href*='/cart']")