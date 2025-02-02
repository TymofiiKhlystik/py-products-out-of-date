from datetime import date
import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "test_outdated_products, expected_products",
    [
        (
            [
                {"name": "Apple", "expiration_date": date(2025, 1, 30)},
                {"name": "Banana", "expiration_date": date(2025, 4, 30)},
                {"name": "Orange", "expiration_date": date(2025, 12, 30)},
            ],
            ["Apple"]
        ),
        (
            [],
            []
        )
    ]
)
def test_outdated_products(
        test_outdated_products: list,
        expected_products: list
) -> None:
    assert outdated_products(test_outdated_products) == expected_products
