"""Ex05 - Tests for List functions."""

__author__ = "730480148"

from utils import only_evens, sub, concat


def test_only_evens_normal() -> None:
    """Tests only_evens for a typical usage of the function."""
    xs: list[int] = [1, 2, 5]
    assert only_evens(xs) == [2] 


def test_only_evens_empty() -> None:
    """Tests only_evens when given an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_odds() -> None:
    """Tests only_evens when given a list with no even elements."""
    xs: list[int] = [1, 3, 3, 5]
    assert only_evens(xs) == []


def test_sub_normal() -> None:
    """Tests sub for a typical usage of the function."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 1, 3) == [20, 30]


def test_sub_empty() -> None:
    """Tests sub when given an empty list."""
    xs: list[int] = []
    assert sub(xs, -1, 1) == []


def test_sub_out_of_bounds() -> None:
    """Tests sub when given indexes that are out of the range of the list."""
    xs: list[int] = [2, 4, 6, 23]
    assert sub(xs, 10, 5) == []


def test_concat_normal() -> None:
    """Tests concat for a typical usage of the function."""
    xs: list[int] = [1, 2, 3, 4]
    ys: list[int] = [3, 2, 1]
    assert concat(xs, ys) == [1, 2, 3, 4, 3, 2, 1]


def test_concat_one_empty() -> None:
    """Tests concat when one list is empty."""
    xs: list[int] = [1, 2, 3, 4]
    ys: list[int] = []
    assert concat(xs, ys) == [1, 2, 3, 4]


def test_concat_both_empty() -> None:
    """Tests concat when both lists are empty."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []