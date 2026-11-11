import allure

from src.core.driver_factory import build_driver


def before_scenario(context, scenario):
    tags = set(scenario.tags) | set(scenario.feature.tags)
    # Pure API scenarios (bookstore) never touch a browser -- skip spinning
    # one up for them.
    if "api" not in tags:
        context.driver = build_driver()


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        if scenario.status == "failed":
            allure.attach(
                context.driver.get_screenshot_as_png(),
                name="screenshot-on-failure",
                attachment_type=allure.attachment_type.PNG,
            )
        context.driver.quit()

    # Self-cleaning: delete the bookstore account even if an assertion
    # failed mid-scenario -- this repo shares demoqa.com's public API with
    # everyone else running these tests.
    if hasattr(context, "bookstore_account"):
        context.bookstore_client.delete_account(context.bookstore_account)
