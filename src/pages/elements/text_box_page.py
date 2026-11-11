from dataclasses import dataclass

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.core.base_page import BasePage
from src.core.config import Config


@dataclass
class TextBoxData:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


class TextBoxPage(BasePage):
    path = "/text-box"

    _FULL_NAME = (By.CSS_SELECTOR, "[placeholder='Full Name']")
    _EMAIL = (By.CSS_SELECTOR, "[placeholder='name@example.com']")
    _CURRENT_ADDRESS = (By.CSS_SELECTOR, "[placeholder='Current Address']")
    # Unlike the other fields on this page, DemoQA gives Permanent Address
    # no placeholder/accessible name -- its raw id is the only selector.
    _PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    _SUBMIT = (By.ID, "submit")
    # #output has no accessible role/label of its own -- DemoQA's id for the result panel.
    _OUTPUT = (By.ID, "output")
    _HEADING = (By.XPATH, "//h1[normalize-space()='Text Box']")

    def wait_for_loaded(self) -> None:
        WebDriverWait(self.driver, Config.EXPLICIT_WAIT_SECONDS).until(
            EC.visibility_of_element_located(self._HEADING)
        )

    def submit(self, data: TextBoxData) -> None:
        self.driver.find_element(*self._FULL_NAME).send_keys(data.full_name)
        self.driver.find_element(*self._EMAIL).send_keys(data.email)
        self.driver.find_element(*self._CURRENT_ADDRESS).send_keys(data.current_address)
        self.driver.find_element(*self._PERMANENT_ADDRESS).send_keys(data.permanent_address)
        self.driver.find_element(*self._SUBMIT).click()

    def expect_submitted(self, data: TextBoxData) -> None:
        output = WebDriverWait(self.driver, Config.EXPLICIT_WAIT_SECONDS).until(
            EC.visibility_of_element_located(self._OUTPUT)
        )
        output_text = output.text
        assert data.full_name in output_text, f"expected full name in output, got: {output_text}"
        assert data.email in output_text, f"expected email in output, got: {output_text}"
        assert data.current_address in output_text, f"expected current address in output, got: {output_text}"
        assert data.permanent_address in output_text, f"expected permanent address in output, got: {output_text}"
