from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BookData:
    isbn: str
    title: str
    author: str
    publisher: str


class BookFactory:
    """DemoQA's public Book Store catalog contains fixed ISBNs. Use known
    catalog records for add-to-collection UI/API scenarios."""

    @staticmethod
    def catalog() -> list[BookData]:
        return [
            BookData(isbn="9781449325862", title="Git Pocket Guide", author="Richard E. Silverman", publisher="O'Reilly Media"),
            BookData(isbn="9781491904244", title="You Don't Know JS", author="Kyle Simpson", publisher="O'Reilly Media"),
            BookData(isbn="9781449331818", title="Learning JavaScript Design Patterns", author="Addy Osmani", publisher="O'Reilly Media"),
        ]

    @staticmethod
    def first() -> BookData:
        return BookFactory.catalog()[0]
