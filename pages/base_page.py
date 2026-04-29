from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # =========================
    # Obsługa kliknięć
    # =========================
    def safe_click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except ElementClickInterceptedException:
            print("Usunięcie overlay")
            self.handle_overlays()
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].click();", element)

    # =========================
    # Obsługa popupów
    # =========================
    def handle_overlays(self):
        self.close_random_popup()
        self.accept_age_if_present()
        self.accept_cookies_if_present()

    # =========================
    # Weryfikacja wieku
    # =========================
    def accept_age_if_present(self):
        try:
            btn = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "verification_btn_accept"))
            )
            self.driver.execute_script("arguments[0].click();", btn)
            print("Wiek potwierdzony")
        except TimeoutException:
            pass

    # =========================
    # Odklikanie cookies
    # =========================
    def accept_cookies_if_present(self):
        try:
            btn = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, "shopify-pc__banner__btn-accept"))
            )

            self.driver.execute_script("arguments[0].click();", btn)
            print("Zaakceptowane Cookies")
        except TimeoutException:
            pass

    # =========================
    # BLOKUJĄCY POPUP
    # =========================
    def close_random_popup(self):
        try:
            self.wait.until(EC.presence_of_element_located(
                (By.ID, "sca-p-popup-main-popup-container")
            ))

            self.driver.execute_script("""
                let el = document.getElementById('sca-p-popup-main-popup-container');
                if (el) el.remove();
            """)

            print("Popup usunięty")
        except TimeoutException:
            pass