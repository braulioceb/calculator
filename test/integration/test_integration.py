import pytest
from unittest.mock import patch

from calculator.app.calculator import calculator


def get_calculator_test_data():
    return [
        (["1", "2", "3"], 5),
        (["2", "1", "1"], 0),
        (["3", "0", "0"], 0),
        (["4", "4", "1"], 4),
        (["4", "1", "0"], "No division by zero is allowed."),
        (["5", "2", "3"], 8),
    ]


@pytest.mark.parametrize(
    "inputs, expected",
    get_calculator_test_data(),
)
def test_calculator(inputs, expected):
    with patch("builtins.input", side_effect=inputs):
        assert calculator() == expected
