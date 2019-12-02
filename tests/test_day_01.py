"""Testing for all the days"""
import unittest
from hypothesis import given
from hypothesis.strategies import integers
from advent_of_code_2019.day_01 import Day01

from typing import Callable


class DayOneTest(unittest.TestCase):
    """
    Testing day one

    Examples Given:

    For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
    For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
    For a mass of 1969, the fuel required is 654.
    For a mass of 100756, the fuel required is 33583.
    """

    def setUp(self) -> None:
        """Today is a new day"""
        self.Day = Day01

    @given(mass=integers(min_value=1))
    def test_ints(self, mass: int) -> None:
        """test that ints work"""
        self.Day.part_one(mass)

    # noinspection PyMethodMayBeStatic
    def execute_example(self, f: Callable) -> None:
        """Run Hypothesis tests"""
        f()
        return f()

    def test_example_01(self) -> None:
        """For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2."""
        mass: int = 12
        fuel: int = 2
        self.assertEqual(self.Day.part_one(mass), fuel, "Incorrect amount of fuel")

    def test_example_02(self) -> None:
        """For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2."""
        mass: int = 14
        fuel: int = 2
        self.assertEqual(self.Day.part_one(mass), fuel, "Incorrect amount of fuel")

    def test_example_03(self) -> None:
        """ For a mass of 1969, the fuel required is 654."""
        mass: int = 1969
        fuel: int = 654
        self.assertEqual(self.Day.part_one(mass), fuel, "Incorrect amount of fuel")

    def test_example_04(self) -> None:
        """For a mass of 100756, the fuel required is 33583."""
        mass: int = 100756
        fuel: int = 33583
        self.assertEqual(self.Day.part_one(mass), fuel, "Incorrect amount of fuel")

    def tearDown(self) -> None:
        """Today is over"""
        ...


if __name__ == "__main__":
    unittest.main()
