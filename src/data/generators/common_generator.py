import random
import string
import uuid

from faker import Faker

_faker = Faker()


class CommonGenerator:
    """Shared primitives: factories compose these instead of duplicating generators."""

    @staticmethod
    def id() -> str:
        return str(uuid.uuid4())

    @staticmethod
    def first_name() -> str:
        return _faker.first_name()

    @staticmethod
    def last_name() -> str:
        return _faker.last_name()

    @staticmethod
    def full_name() -> str:
        return _faker.name()

    @staticmethod
    def email() -> str:
        return f"qa.{uuid.uuid4()}@example.com"

    @staticmethod
    def username() -> str:
        suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=12))
        return f"qa_{suffix}"

    @staticmethod
    def password() -> str:
        middle = "".join(random.choices(string.ascii_letters + string.digits, k=12))
        return f"Qa!{middle}9"

    @staticmethod
    def phone() -> str:
        return "".join(random.choices(string.digits, k=10))

    @staticmethod
    def address() -> str:
        return _faker.street_address()

    @staticmethod
    def city() -> str:
        return _faker.city()

    @staticmethod
    def date_of_birth():
        return _faker.date_of_birth(minimum_age=18, maximum_age=45)

    @staticmethod
    def integer(minimum: int, maximum: int) -> int:
        return random.randint(minimum, maximum)

    @staticmethod
    def pick(values):
        return random.choice(values)
