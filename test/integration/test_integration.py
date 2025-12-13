import pytest
from calculator.app.calculator import calculator
from unittest.mock import patch

def get_data_test_calculator():
    return     [
        (["1", "2", "3"], 5), 
        (["2", "1", "1"], 0), 
        (["3", "0", "0"], 0), 
        (["4", "4", "1"], 4),
        (["4", "1", "0"], "No division by zero is allowed."),
        (["6", "4", "2"], 2)
    ]

@pytest.mark.parametrize(
    "inputs, expected",
    get_data_test_calculator()
)
def test_add_numbers(inputs, expected):
    with patch("builtins.input", side_effect=inputs):
        assert calculator() == expected