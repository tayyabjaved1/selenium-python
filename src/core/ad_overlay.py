from selenium.webdriver.remote.webdriver import WebDriver

_REMOVE_SELECTORS = ["#fixedban", "iframe[id^='google_ads']"]


class AdOverlay:
    """demoqa.com renders ad banners/iframes that intercept clicks on
    elements they visually overlap. There is no DOM signal distinguishing
    "ad is present" from "ad is absent" other than the elements existing at
    all, so this removes them outright rather than trying to scroll around
    or wait them out."""

    @staticmethod
    def dismiss_if_present(driver: WebDriver) -> None:
        driver.execute_script(
            """
            document.querySelectorAll(arguments[0].join(',')).forEach(el => el.remove());
            """,
            _REMOVE_SELECTORS,
        )
