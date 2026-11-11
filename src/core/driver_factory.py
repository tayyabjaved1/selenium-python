from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.core.config import Config


def build_driver() -> webdriver.Chrome:
    options = Options()
    if Config.HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,900")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Selenium Manager (bundled since 4.6) resolves the matching chromedriver
    # automatically -- no manual driver binary management needed.
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(Config.IMPLICIT_WAIT_SECONDS)
    return driver
