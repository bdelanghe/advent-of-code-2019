"""making sure the the package is in order"""
from advent_of_code_2019 import __version__


def test_version() -> None:
    """checking if the version is good"""
    assert __version__ == '0.1.0'
