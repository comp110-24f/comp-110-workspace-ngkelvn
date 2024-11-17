"""Testing the max function"""

__author__ = "730654182"

from CQs.cq07.find_max import find_and_remove_max


# Test if it returns the expected max value
def test_find_and_remove_max_return() -> None:
    b = [1, 10]
    assert find_and_remove_max(b) == 10  # Checks the returned value
    assert b == [1]


# Test if it mutates the input list as expected
def test_find_and_remove_max_mutate() -> None:
    c = [1, 9, 9, 2]
    find_and_remove_max(c)
    assert c == [1, 2]


# Test if it handles an empty list correctly
def test_find_and_remove_max_empty_list() -> None:
    d = []
    assert find_and_remove_max(d) == -1
    assert d == []
