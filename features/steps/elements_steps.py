from behave import given, then, when

from src.data.factories.form_factory import FormFactory
from src.pages.elements.text_box_page import TextBoxPage


@given("I open the Text Box page")
def step_open_text_box(context):
    context.text_box_page = TextBoxPage(context.driver).open()


@when("I submit the text box form with generated data")
def step_submit_text_box(context):
    context.text_box_data = FormFactory.text_box()
    context.text_box_page.submit(context.text_box_data)


@then("the output panel should show the submitted data")
def step_expect_text_box_output(context):
    context.text_box_page.expect_submitted(context.text_box_data)
