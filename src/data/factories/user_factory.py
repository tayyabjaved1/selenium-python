from __future__ import annotations

from dataclasses import dataclass

from src.data.generators.common_generator import CommonGenerator as gen


@dataclass
class UserData:
    id: str
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    role: str


class UserFactory:
    @staticmethod
    def create(overrides: dict | None = None, role: str = "student") -> UserData:
        overrides = overrides or {}
        base = {
            "id": gen.id(),
            "first_name": gen.first_name(),
            "last_name": gen.last_name(),
            "username": gen.username(),
            "email": gen.email(),
            "password": gen.password(),
            "role": role,
        }
        base.update(overrides)
        return UserData(**base)

    @staticmethod
    def admin(overrides: dict | None = None) -> UserData:
        overrides = overrides or {}
        return UserFactory.create({**overrides, "role": "admin"}, "admin")

    @staticmethod
    def bookstore_user(overrides: dict | None = None) -> UserData:
        return UserFactory.create(overrides, "bookstore-user")
