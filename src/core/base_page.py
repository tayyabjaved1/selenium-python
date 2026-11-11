from abc import ABC, abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver

from src.core.ad_overlay import AdOverlay
from src.core.config import Config


class BasePage(ABC):
    """Every page object implements `path` and `wait_for_loaded()`; `open()`
    is the one shared entrypoint so ad-dismissal and the loaded-wait always
    happen together, in order, for every page -- a caller cannot forget one."""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    @abstractmethod
    def path(self) -> str:
        ...

    @abstractmethod
    def wait_for_loaded(self) -> None:
        ...

    def open(self) -> "BasePage":
        self.driver.get(f"{Config.BASE_URL}{self.path}")
        AdOverlay.dismiss_if_present(self.driver)
        self.wait_for_loaded()
        return self
