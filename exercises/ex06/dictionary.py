"""Ex06 - Dictionary functions: invert, count, favorite_colors."""

__author__ = "730480148"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Returns a dictionary that inverts the keys and values of the input dictionary."""
    output: dict[str, str] = dict()
    for key in d:
        for a in output:
            if d[key] == a:
                raise KeyError
        output[d[key]] = key
    return output


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the color that appears the most frequently in a given dictionary."""
    winner = ""
    frequency: dict[str, int] = {}
    times: int = 0
    for color in colors:
        if colors[color] in frequency:
            frequency[colors[color]] += 1
        else:
            frequency[colors[color]] = 1
    for key in frequency:
        if frequency[key] > times:
            winner = key
            times = frequency[key]
    return winner


def count(xs: list[str]) -> dict[str, int]:
    """Returns a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    counts: dict[str, int] = {}
    for i in xs:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts