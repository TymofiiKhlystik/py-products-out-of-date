import datetime
from unittest.mock import patch

from app.main import outdated_products


def test_outdated_products() -> None:
    test_products = [
        {"name": "Apple", "expiration_date": datetime.date(2021, 1, 30)},
        {"name": "Banana", "expiration_date": datetime.date(2025, 4, 30)},
        {"name": "Orange", "expiration_date": datetime.date(2025, 12, 30)},
    ]

    fake_today = datetime.date(2022, 2, 5)

    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = fake_today
        assert outdated_products(test_products) == ["Apple"]
