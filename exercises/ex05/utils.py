"""Ex05 - List functions: only_evens, sub, concat."""

__author__ = "730480148"


def only_evens(xs: list[int]) -> list[int]:
    """Returns a list of integers containing only the even elements of the input parameter."""
    evens: list[int] = list()
    for x in xs:
        if xs[i] % 2 == 0:
            evens.append(xs[i])
    return evens


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Returns a list that is a subset of the given list, between the specified indexes."""
    subset: list[int] = list()
    if start < end - 1:
        while start < end - 1:
            subset.append(xs[start])
            start += 1
    elif start == end:
        subset.append(xs[start])
        return subset