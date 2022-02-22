"""Ex05 - List functions: only_evens, sub, concat."""

__author__ = "730480148"


def only_evens(xs: list[int]) -> list[int]:
    """Returns a list of integers containing only the even elements of the input list."""
    evens: list[int] = list()
    # for each item in the list, check to see if there is a remainder when divided by two
    for x in xs:
        # no remainder means the item is even and should be added to the list that will be returned
        if x % 2 == 0:
            evens.append(x)
    return evens


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Returns a list that is a subset of the given list, between the specified indexes, not inclusive at the end index."""
    subset: list[int] = list()
    # set starting index to zero if it is negative
    if start < 0:
        start = 0
    # set ending index to the length of the list if it is greater than that value
    if end > len(xs):
        end = len(xs)
    # return an empty list if given unrealistic parameters
    if len(xs) == 0 or start > len(xs) or end <= 0:
        return subset
    # while the starting index is less than the ending index, add the element at that index
    # to the list to be returned
    while start < end:
        subset.append(xs[start])
        start += 1
    return subset


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Returns a list containing all of the elements of the first list followed by all of the elements of the second list."""
    combined: list[int] = list()
    # add each element in the first list to the list to be returned
    for x in xs:
        combined.append(x)
    # then add each element in the second list to the list to be returned, after the first list
    for y in ys:
        combined.append(y)
    return combined