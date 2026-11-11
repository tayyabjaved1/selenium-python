from __future__ import annotations

from src.data.generators.common_generator import CommonGenerator as gen
from src.pages.elements.text_box_page import TextBoxData


class FormFactory:
    @staticmethod
    def text_box(overrides: dict | None = None) -> TextBoxData:
        overrides = overrides or {}
        base = {
            "full_name": gen.full_name(),
            "email": gen.email(),
            "current_address": gen.address(),
            "permanent_address": gen.address(),
        }
        base.update(overrides)
        return TextBoxData(**base)
