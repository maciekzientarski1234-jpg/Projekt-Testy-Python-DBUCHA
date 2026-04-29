from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EntryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def accept_age(self):
        try:
            btn = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".verification_btn_accept"))
            )
            btn.click()
            print("Kliknięto 18+")
        except:
            print("Brak popupu 18+")

    def accept_cookies(self):
        try:
            btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Akceptuj')]"))
            )
            btn.click()
            print("Cookies zaakceptowane")
        except:
            print("Brak cookies")

    def handle_all(self):
        self.accept_age()
        self.accept_cookies()