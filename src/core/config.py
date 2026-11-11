import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_URL = os.getenv("BASE_URL", "https://demoqa.com")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    BROWSER = os.getenv("BROWSER", "chrome")
    IMPLICIT_WAIT_SECONDS = float(os.getenv("IMPLICIT_WAIT_SECONDS", "0"))
    EXPLICIT_WAIT_SECONDS = float(os.getenv("EXPLICIT_WAIT_SECONDS", "10"))
