from behave import given, then, when

from src.api.bookstore_client import BookStoreClient
from src.core.config import Config
from src.data.factories.book_factory import BookFactory
from src.data.factories.user_factory import UserFactory


@given("a unique bookstore account exists")
def step_create_bookstore_account(context):
    context.bookstore_client = BookStoreClient(Config.BASE_URL)
    user = UserFactory.bookstore_user()
    context.bookstore_account = context.bookstore_client.create_account(user)
    # Deleted in environment.py's after_scenario so a failed assertion still
    # cleans up the account -- this repo shares demoqa.com with everyone.


@when("I add the first catalog book to the account")
def step_add_catalog_book(context):
    context.book = BookFactory.first()
    context.bookstore_client.add_book(context.bookstore_account, context.book.isbn)


@then("the book should appear in the account collection")
def step_expect_book_in_collection(context):
    collection = context.bookstore_client.get_books(context.bookstore_account)
    isbns = [item["isbn"] for item in collection["books"]]
    assert context.book.isbn in isbns, f"expected {context.book.isbn} in {isbns}"
