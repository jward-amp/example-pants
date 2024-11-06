import pytest

from project2.fizzbuzz import buzz, fizz


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, ""),
        (2, ""),
        (3, "Fizz"),
        (4, ""),
        (5, ""),
        (6, "Fizz"),
    ],
)
def test_fizz(n, expected):
    assert fizz(n) is expected


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, ""),
        (2, ""),
        (3, ""),
        (4, ""),
        (5, "Buzz"),
        (6, ""),
        (10, "Buzz"),
    ],
)
def test_buzz(n, expected):
    assert buzz(n) is expected
