"""Ex06 - Tests for Dictionary functions."""

__author__ = "730480148"

import pytest
from dictionary import invert, favorite_color, count


def test_invert_normal() -> None:
    """Tests invert for a standard use of the function."""
    my_dictionary: dict[str, str] = {"a": "b", "c": "d"}
    assert invert(my_dictionary) == {"b": "a", "d": "c"}
    

def test_invert_same_key() -> None:
    """Tests invert when the input dictionary has more than one of the same key."""
    with pytest.raises(KeyError):
        my_dictionary: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_invert_empty() -> None:
    """Tests invert when the input dictionary is empty."""
    my_dictionary: dict[str, str] = dict()
    invert(my_dictionary)


def test_favorite_color_normal() -> None:
    """Tests favorite_color for a standard use of the function."""
    colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(colors) == "blue"


def test_favorite_color_tie() -> None:
    """Tests favorite_color for when there is a tie in favorite colors."""
    colors: dict[str, str] = {"Marc": "pink", "Kyle": "pink", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(colors) == "pink"


def test_favorite_color_empty() -> None:
    """Tests favorite_color for when there are no favorite colors."""
    colors: dict[str, str] = {}
    assert favorite_color(colors) == ""


def test_count_normal() -> None:
    """Tests count for a standard use of the function."""
    xs = ["hey", "hi", "hello", "hi", "hi"]
    assert count(xs) == {"hey": 1, "hi": 3, "hello": 1}


def test_count_single() -> None:
    """Tests count for a list with one item."""
    xs = ["hey"]
    assert count(xs) == {"hey": 1}


def test_count_empty() -> None:
    """Tests count for when it is given an empty list."""
    xs: list[str] = []
    assert count(xs) == {}