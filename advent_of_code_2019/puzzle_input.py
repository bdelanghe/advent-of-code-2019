"""Import input and convert it to a list"""
import os.path
from typing import Any, Iterable


def get_input(day: str) -> Iterable[Any]:
    """get input for a given day"""
    with open(f'{os.path.dirname(__file__)}/../input/{day}.txt') as f:
        for line in f:
            yield line[:-1]


if __name__ == '__main__':
    for l in get_input('day01'):
        print(l)
