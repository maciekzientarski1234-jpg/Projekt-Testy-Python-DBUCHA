from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_driver():
    options = webdriver.ChromeOptions()

    options.binary_location = "/snap/bin/chromium"

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(
        service=Service("/usr/local/bin/chromedriver"),
        options=options
    )

    return driver