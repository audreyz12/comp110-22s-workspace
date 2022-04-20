"""Practice for quiz03!"""

from __future__ import annotations


class ChristmasTreeFarm:
    """A class for a Christmas Tree Farm."""
    plots: list[int]

    def __init__(self, plots: int, initial_planting: int) -> None:
        """Constructor."""
        self.plots = []
        i: int = 0
        while i < initial_planting:
            self.plots.append(1)
            i += 1
        while i < plots:
            self.plots.append(0)
            i += 1

    def plant(self, plot_number: int) -> None:
        """Plants a tree at the given plot number."""
        self.plots[plot_number] = 1

    def growth(self) -> None:
        """Grows each planted tree."""
        i: int = 0
        while i < len(self.plots):
            if self.plots[i] != 0:
                self.plots[i] += 1
            i += 1

    def harvest(self, replant: bool) -> int:
        """Harvest trees that are fully grown!"""
        total: int = 0
        i: int = 0
        while i < len(self.plots):
            if self.plots[i] >= 5:
                total += 1
                if replant:
                    self.plots[i] = 1
                else:
                    self.plots[i] = 0
            i += 1
        return total

    def __add__(self, rhs: ChristmasTreeFarm) -> ChristmasTreeFarm:
        """Overload addition to create a new ChristmasTreeFarm."""
        trees: int = 0
        for plot in self.plots:
            if plot > 0:
                trees += 1
        for plot in rhs.plots:
            if plot > 0:
                trees += 1
        return ChristmasTreeFarm(len(self.plots + rhs.plots), trees)


class Course:
    """Models the idea of a UNC course."""
    name: str
    level: int
    prerequisites: list[str]

    def find_courses(self, listy: list[Course], prereq: str) -> list[str]:
        result: list[str] = []
        for course in listy:
            if course.level >= 400:
                for p in course.prerequisites:
                    if p == prereq:
                        result.append(course.name)
        return result

    def is_valid_course(self, prereq: str) -> bool:
        if self.level < 400:
            return False
        else:
            for p in self.prerequisites:
                if p == prereq:
                    return True
            return False
