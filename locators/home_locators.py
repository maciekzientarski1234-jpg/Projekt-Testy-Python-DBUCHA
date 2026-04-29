from selenium.webdriver.common.by import By

class HomeLocators:
    PRODUCTS = (By.CSS_SELECTOR, "a[href*='/products/']")