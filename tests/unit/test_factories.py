from src.data.builders.student_builder import StudentBuilder
from src.data.factories.book_factory import BookFactory
from src.data.factories.student_factory import StudentFactory
from src.data.factories.user_factory import UserFactory


def test_creates_unique_runtime_user_data():
    first = UserFactory.create()
    second = UserFactory.create()
    assert first.email != second.email
    assert first.username != second.username
    assert first.id != second.id


def test_supports_role_presets_and_scenario_overrides():
    admin = UserFactory.admin()
    student = StudentFactory.create({"gender": "Female"})
    assert admin.role == "admin"
    assert student.gender == "Female"


def test_builds_scenario_data_fluently():
    student = StudentBuilder().with_gender("Other").with_address("221B Baker Street").build()
    assert student.gender == "Other"
    assert student.address == "221B Baker Street"


def test_book_catalog_is_stable_and_first_matches_catalog_head():
    catalog = BookFactory.catalog()
    assert len(catalog) == 3
    assert BookFactory.first() == catalog[0]
    assert all(book.isbn for book in catalog)
