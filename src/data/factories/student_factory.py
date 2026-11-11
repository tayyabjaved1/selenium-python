from __future__ import annotations

from src.data.generators.common_generator import CommonGenerator as gen
from src.pages.forms.practice_form_page import StudentData


class StudentFactory:
    @staticmethod
    def create(overrides: dict | None = None) -> StudentData:
        overrides = overrides or {}
        birth = gen.date_of_birth()
        base = {
            "first_name": gen.first_name(),
            "last_name": gen.last_name(),
            "email": gen.email(),
            "gender": gen.pick(["Male", "Female", "Other"]),
            "mobile": gen.phone(),
            "date_of_birth": f"{birth.day} {birth.strftime('%b')} {birth.year}",
            "address": gen.address(),
        }
        base.update(overrides)
        return StudentData(**base)
