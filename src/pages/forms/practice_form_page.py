from dataclasses import dataclass

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.core.ad_overlay import AdOverlay
from src.core.base_page import BasePage
from src.core.config import Config


@dataclass
class StudentData:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth: str
    address: str


class PracticeFormPage(BasePage):
    path = "/automation-practice-form"

    _FIRST_NAME = (By.CSS_SELECTOR, "[placeholder='First Name']")
    _LAST_NAME = (By.CSS_SELECTOR, "[placeholder='Last Name']")
    _EMAIL = (By.CSS_SELECTOR, "[placeholder='name@example.com']")
    _MOBILE = (By.CSS_SELECTOR, "[placeholder='Mobile Number']")
    # DemoQA's gender/hobbies radios are visually hidden; only their <label>
    # is interactable -- clicking the (invisible, zero-size) input itself
    # raises an ElementNotInteractableException.
    _GENDER_LABEL = "//label[normalize-space()='{}']"
    # react-datepicker's input exposes no accessible label/placeholder of its own.
    _DOB_INPUT = (By.ID, "dateOfBirthInput")
    _CURRENT_ADDRESS = (By.CSS_SELECTOR, "[placeholder='Current Address']")
    _SUBMIT = (By.ID, "submit")
    # Bootstrap's modal component exposes no accessible name distinguishing it from other dialogs.
    _MODAL = (By.CLASS_NAME, "modal-content")
    _HEADING = (By.XPATH, "//h1[normalize-space()='Practice Form']")

    def wait_for_loaded(self) -> None:
        WebDriverWait(self.driver, Config.EXPLICIT_WAIT_SECONDS).until(
            EC.visibility_of_element_located(self._HEADING)
        )

    def submit(self, student: StudentData) -> None:
        self.driver.find_element(*self._FIRST_NAME).send_keys(student.first_name)
        self.driver.find_element(*self._LAST_NAME).send_keys(student.last_name)
        self.driver.find_element(*self._EMAIL).send_keys(student.email)
        self.driver.find_element(By.XPATH, self._GENDER_LABEL.format(student.gender)).click()
        self.driver.find_element(*self._MOBILE).send_keys(student.mobile)

        # Clearing this field via .clear() nulls react-datepicker's internal
        # state and crashes the whole page -- select-all + overtype instead.
        dob = self.driver.find_element(*self._DOB_INPUT)
        dob.send_keys(Keys.CONTROL, "a")
        dob.send_keys(student.date_of_birth)
        dob.send_keys(Keys.ENTER)

        self.driver.find_element(*self._CURRENT_ADDRESS).send_keys(student.address)

        # DemoQA's ad slots reload asynchronously as the page is scrolled
        # through, so a blocker can appear at the Submit button's exact
        # coordinates between the scroll and the click even though
        # dismiss_if_present() just ran and found nothing to remove -- the
        # intercept is a race, not a fixed element. A JS click bypasses the
        # browser's own visibility/overlap check entirely, so it still fires
        # even if an ad is transiently covering the button on-screen.
        submit = self.driver.find_element(*self._SUBMIT)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit)
        AdOverlay.dismiss_if_present(self.driver)
        try:
            submit.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", submit)

    def expect_submission(self, student: StudentData) -> None:
        modal = WebDriverWait(self.driver, Config.EXPLICIT_WAIT_SECONDS).until(
            EC.visibility_of_element_located(self._MODAL)
        )
        modal_text = modal.text
        full_name = f"{student.first_name} {student.last_name}"
        assert full_name in modal_text, f"expected '{full_name}' in modal, got: {modal_text}"
        assert student.email in modal_text, f"expected email in modal, got: {modal_text}"
        assert student.mobile in modal_text, f"expected mobile in modal, got: {modal_text}"
