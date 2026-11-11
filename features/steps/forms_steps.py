from behave import given, then, when

from src.data.factories.student_factory import StudentFactory
from src.pages.forms.practice_form_page import PracticeFormPage


@given("I open the Practice Form page")
def step_open_practice_form(context):
    context.practice_form_page = PracticeFormPage(context.driver).open()


@when("I submit the generated student profile")
def step_submit_practice_form(context):
    context.student = StudentFactory.create()
    context.practice_form_page.submit(context.student)


@then("the confirmation modal should show the submitted profile")
def step_expect_practice_form_modal(context):
    context.practice_form_page.expect_submission(context.student)
