from src.data.factories.student_factory import StudentFactory
from src.pages.forms.practice_form_page import StudentData


class StudentBuilder:
    """Fluent builder for scenario-specific data without creating one factory per scenario."""

    def __init__(self):
        self._overrides: dict = {}

    def with_gender(self, gender: str) -> "StudentBuilder":
        self._overrides["gender"] = gender
        return self

    def with_address(self, address: str) -> "StudentBuilder":
        self._overrides["address"] = address
        return self

    def build(self) -> StudentData:
        return StudentFactory.create(self._overrides)
