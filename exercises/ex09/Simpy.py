"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730480148"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructor."""
        self.values = values

    def __str__(self) -> str:
        """String method."""
        return f"Simpy({self.values})"

    def fill(self, floaty: float, times: int) -> None:
        """Fills a Simpy's values with a specific number of repeating values."""
        self.values: list[float] = []
        for i in range(0, times):
            self.values.append(floaty)
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills Simpy's values with a range of floats."""
        assert step != 0.0
        self.values.append(start)
        if step > 0:
            while start < stop - step:
                self.values.append(start + step)
                start += step 
        else:
            while stop < start + step:
                self.values.append(start + step)
                start += step 

    def sum(self) -> float:
        """Returns the sum of all items in the value attribute."""
        total: float = sum(self.values)
        return total

    def __add__(self, other: Union[float, Simpy]) -> Simpy:
        """Add method."""
        result: Simpy = Simpy([])
        if isinstance(other, float):
            for item in self.values:
                result.values.append(item + other)
        else:
            assert len(self.values) == len(other.values)
            for i in range(0, len(self.values)):
                result.values.append(self.values[i] + other.values[i])
        return result

    def __pow__(self, other: Union[float, Simpy]) -> Simpy:
        """Power operator."""
        result: Simpy = Simpy([])
        if isinstance(other, float):
            for item in self.values:
                result.values.append(item ** other)
        else:
            assert len(self.values) == len(other.values)
            for i in range(0, len(self.values)):
                result.values.append(self.values[i] ** other.values[i])
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Equality operator."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            for i in range(0, len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Greater than operator that creates a mask."""
        mask: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    mask.append(True)
                else:
                    mask.append(False)
        else:
            for i in range(0, len(self.values)):
                if self.values[i] > rhs.values[i]:
                    mask.append(True)
                else:
                    mask.append(False)
        return mask

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Subscription operator that filters with a mask."""
        if isinstance(rhs, int):
            number: float = 0.0
            number = self.values[rhs]
            return number
        else:
            output: Simpy = Simpy([])
            for i in range(0, len(self.values)):
                if rhs[i]:
                    output.values.append(self.values[i])
            return output