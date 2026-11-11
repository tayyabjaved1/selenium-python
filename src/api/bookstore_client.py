from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import requests


@dataclass
class UserData:
    username: str
    password: str


@dataclass
class BookStoreAccount:
    user_id: str
    token: str
    user: UserData


class BookStoreClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def create_account(self, user: UserData) -> BookStoreAccount:
        response = requests.post(
            f"{self.base_url}/Account/v1/User",
            json={"userName": user.username, "password": user.password},
        )
        if not response.ok:
            raise RuntimeError(f"DemoQA account creation failed ({response.status_code}): {response.text}")
        created = response.json()

        token_response = requests.post(
            f"{self.base_url}/Account/v1/GenerateToken",
            json={"userName": user.username, "password": user.password},
        )
        if not token_response.ok:
            raise RuntimeError(f"DemoQA token generation failed ({token_response.status_code}): {token_response.text}")
        token_data = token_response.json()
        if not token_data.get("token"):
            raise RuntimeError(f"DemoQA did not return an auth token: {token_data}")

        return BookStoreAccount(user_id=created["userID"], token=token_data["token"], user=user)

    def add_book(self, account: BookStoreAccount, isbn: str) -> None:
        response = requests.post(
            f"{self.base_url}/BookStore/v1/Books",
            headers={"Authorization": f"Bearer {account.token}"},
            json={"userId": account.user_id, "collectionOfIsbns": [{"isbn": isbn}]},
        )
        if not response.ok:
            raise RuntimeError(f"Adding book failed ({response.status_code}): {response.text}")

    def get_books(self, account: BookStoreAccount) -> dict[str, Any]:
        response = requests.get(
            f"{self.base_url}/BookStore/v1/Books",
            params={"UserId": account.user_id},
            headers={"Authorization": f"Bearer {account.token}"},
        )
        if not response.ok:
            raise RuntimeError(f"Fetching book collection failed ({response.status_code}): {response.text}")
        return response.json()

    def delete_account(self, account: BookStoreAccount) -> None:
        response = requests.delete(
            f"{self.base_url}/Account/v1/User/{account.user_id}",
            headers={"Authorization": f"Bearer {account.token}"},
        )
        # 404 can mean the account has already been removed; other errors should be visible.
        if not response.ok and response.status_code != 404:
            raise RuntimeError(f"Account cleanup failed ({response.status_code}): {response.text}")
