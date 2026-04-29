from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
import random
import time


class ProductPage(BasePage):

    def select_random_variant(self):
        try:
            select = Select(self.wait.until(
                lambda d: d.find_element(By.TAG_NAME, "select")
            ))

            options = [o for o in select.options if o.get_attribute("disabled") is None]

            choice = random.choice(options)
            select.select_by_visible_text(choice.text)

            print(f"Wybrano wariant: {choice.text}")
        except:
            print("Brak wariantów")

    def increase_quantity(self):
        for _ in range(2):  # razem 3 sztuki
            self.safe_click((By.NAME, "plus"))

    def add_to_cart(self):
        self.handle_overlays()

        self.select_random_variant()
        self.increase_quantity()

        print("Dodaję produkt do koszyka...")
        self.safe_click((By.NAME, "add"))

    def go_to_checkout_popup(self):
        time.sleep(2)
        self.handle_overlays()

        print("Klikam REALIZUJ ZAKUP z popupu")
        self.safe_click((By.NAME, "checkout"))