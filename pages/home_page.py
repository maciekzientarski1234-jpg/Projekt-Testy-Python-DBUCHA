from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from pages.base_page import BasePage


class HomePage(BasePage):

    def open_home(self):
        self.driver.get("https://www.dbucha.com")

        print("Rozwiąż CAPTCHA jeśli jest")
        time.sleep(10)

        # 🔥 popupy często ładują się z opóźnieniem
        self.handle_overlays()
        time.sleep(1)
        self.handle_overlays()

    def open_products(self):
        self.handle_overlays()

        print("Otwieram listę produktów")

        btn = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//a[contains(@href,'/collections/jednorazowki')]")
        ))

        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)

        try:
            btn.click()
        except:
            print("Kliknięcie listy produktów")
            self.handle_overlays()
            self.driver.execute_script("arguments[0].click();", btn)

    def open_first_product(self):
        self.handle_overlays()

        print("Wyszukanie produktu")

        product = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a.product-name-text")
        ))

        self.driver.execute_script("arguments[0].scrollIntoView(true);", product)
        time.sleep(1)

        try:
            product.click()
        except:
            print("Wybranie produktu")
            self.handle_overlays()
            self.driver.execute_script("arguments[0].click();", product)

        print("Wybranie produktu")