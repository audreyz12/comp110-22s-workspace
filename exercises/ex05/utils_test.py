"""Ex05 - Tests for List functions."""

__author__ = "730480148"

from exercises.ex05.utils import only_evens


def test_only_evens() -> None:
    xs: list[int] = [1, 2, 5]
    assert only_evens(xs) == [2] 


def test_only_evens_empty() -> None:
    xs: list[int] = []
    assert only_evens(xs) == []