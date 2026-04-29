from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import random
import string
import time


class CheckoutPage(BasePage):

    def fill_fake_data(self):
        def rand():
            return ''.join(random.choices(string.ascii_lowercase, k=6))

        time.sleep(3)

        self.driver.find_element(By.NAME, "email").send_keys(f"{rand()}@mail.com")
        self.driver.find_element(By.NAME, "firstName").send_keys("Jan")
        self.driver.find_element(By.NAME, "lastName").send_keys("Kowalski")
        self.driver.find_element(By.NAME, "address1").send_keys("Testowa 1")
        self.driver.find_element(By.NAME, "postalCode").send_keys("00-001")
        self.driver.find_element(By.NAME, "city").send_keys("Warszawa")

        print("🧾 Wypełniono dane")