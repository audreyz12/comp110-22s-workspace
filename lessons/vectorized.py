from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items
    
    def __repr__(self) -> str:
        return f"StrArray{self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        """Vectorized concatenation operator."""
        # Setup a result list of strings that's empty
        # Loop through each item in self.items
        # For each item, append the concatenation of item and rhs to result list
        # Return a newly constructed StrArray whose items are result
        result: list[str] = []
        if isinstance(rhs, str):
            for item in self.items:
                result.append(item + rhs)
        else:
            # Assert that len of self.items is equal to the length of rhs.items
            assert len(self.items) == len(rhs.items)
            # Build up the result list by concatenating
            # each item in self.items with corresponding item in rhs.items
            for i in range(0, len(self.items)):
                result.append(self.items[i] + rhs.items[i])
        return StrArray(result)


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
result: StrArray = first + "!"
print(result)
print(first + " " + last)
print(last + " , " + first + "!!!")