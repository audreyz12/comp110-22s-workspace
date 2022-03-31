"""Dictionary related utility functions."""

__author__ = "730480148"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first n rows of data for each column."""
    result: dict[str, list[str]] = {}
    i: int = 0
    if n > len(table):
        n = len(table)
    for item in table:
        data: list[str] = []
        i = 0
        while i < n:
            data.append(table[item][i])
            result[item] = data
            i += 1
        if n == 0:
            result[item] = []
    return result


def select(table: dict[str, list[str]], copy: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for item in copy:
        result[item] = table[item]
    return result


def count(listy: list[str]) -> dict[str, int]:
    """Produces a dict[str, int] where each key is a unique value in the given list and each value is the count of the number of times the value appears in the input list."""
    result: dict[str, int] = {}
    for item in listy:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def add(dicty: dict[str, int]) -> int:
    """Produces an integer sum of all the values in a dict[str, int]."""
    result: int = 0
    for item in dicty:
        result += dicty[item]
    return result


def proportions(dicty: dict[str, int], total: int) -> dict[str, float]:
    """Given a dict[str, int], produces a new dictionary containing proportions."""
    result: dict[str, float] = {}
    for item in dicty:
        result[item] = dicty[item] / total 
    return result