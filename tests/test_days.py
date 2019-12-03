"""Testing for all the days"""
import unittest
from typing import Any, Callable

# noinspection Mypy
from hypothesis import given
# noinspection Mypy
from hypothesis.strategies import integers

from advent_of_code_2019.days import *


class DayOneTest(unittest.TestCase):
    """
    Part One Examples Given:

    For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
    For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
    For a mass of 1969, the fuel required is 654.
    For a mass of 100756, the fuel required is 33583.

    Part two Examples Given:

    At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2).
    216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel.
    So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.

    The fuel required by a module of mass 100756 and its fuel is:
    33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
    """

    def setUp(self) -> None:
        """Today is a new day"""
        self.Day = Day01()

    # noinspection Mypy
    @given(module_mass=integers(min_value=1))
    def test_part1_ints(self, module_mass: int) -> None:
        """test that ints work"""
        self.Day.mass_fuel_needed(module_mass)

    # noinspection PyMethodMayBeStatic
    def execute_example(self, f: Callable[..., Any]) -> Any:
        """Run Hypothesis tests"""
        f()
        return f()

    def test_part1_example01(self) -> None:
        """For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2."""
        module_mass: int = 12
        module_fuel: int = 2
        self.assertEqual(
            self.Day.mass_fuel_needed(module_mass),
            module_fuel,
            "Incorrect amount of module_fuel",
        )

    def test_part1_example02(self) -> None:
        """For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2."""
        module_mass: int = 14
        module_fuel: int = 2
        self.assertEqual(
            self.Day.mass_fuel_needed(module_mass),
            module_fuel,
            "Incorrect amount of module_fuel",
        )

    def test_part1_example03(self) -> None:
        """ For a mass of 1969, the fuel required is 654."""
        module_mass: int = 1969
        module_fuel: int = 654
        self.assertEqual(
            self.Day.mass_fuel_needed(module_mass),
            module_fuel,
            "Incorrect amount of module_fuel",
        )

    def test_part1_example04(self) -> None:
        """For a mass of 100756, the fuel required is 33583."""
        module_mass: int = 100756
        module_fuel: int = 33583
        self.assertEqual(
            self.Day.mass_fuel_needed(module_mass),
            module_fuel,
            "Incorrect amount of module_fuel",
        )

    def test_part2_example01(self) -> None:
        """
        A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0,
        which would call for a negative fuel), so the total fuel required is still just 2.
        """
        module_mass: int = 14
        total_fuel: int = 2
        self.assertEqual(
            self.Day.total_fuel_needed(module_mass),
            total_fuel,
            "Incorrect amount of module_fuel",
        )

    def test_part2_example02(self) -> None:
        """
        At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2).
        216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel.
        So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
        """
        module_mass: int = 1969
        total_fuel: int = 966
        self.assertEqual(
            self.Day.total_fuel_needed(module_mass),
            total_fuel,
            "Incorrect amount of module_fuel",
        )

    def test_part2_example03(self) -> None:
        """
        The fuel required by a module of mass 100756 and its fuel is:
        33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
        """
        module_mass: int = 100756
        total_fuel: int = 50346
        self.assertEqual(
            self.Day.total_fuel_needed(module_mass),
            total_fuel,
            "Incorrect amount of module_fuel",
        )

    def test_compare(self) -> None:
        """Grand total should be greater than module"""
        grand_total = self.Day.grand_total_fuel
        module_total = self.Day.module_total_fuel
        self.assertGreaterEqual(
            grand_total,
            module_total,
            "Grand Total should be equal or greater than module total",
        )

    def tearDown(self) -> None:
        """Today is over"""
        ...


if __name__ == "__main__":
    unittest.main()
