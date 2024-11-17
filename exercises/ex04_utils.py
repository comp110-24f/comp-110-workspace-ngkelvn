"""Utility functions for list operations."""

__author__ = "730654182"


def all(lst: list[int], x: int) -> bool:
    """Returns true if all the elements in the list match x."""
    for element in lst:
        # if all the elements do not match the given x int value, false is returned.
        if element != x:
            return False

    if len(lst) == 0:  # if the list is empty, false is returned.
        return False

    return True


def max(input: list[int]) -> int:
    """Checks for the largest input in the list."""
    if len(input) == 0:
        assert ValueError

    largest = input[0]
    for number in input:
        if number > largest:
            largest = number

    return largest


def is_equal(lst1: list[int], lst2: list[int]) -> bool:
    """Returns true if both lists have same elements in the same order."""
    if len(lst1) != len(lst2):
        return False

    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False

    return True


def extend(lst1: list[int], lst2: list[int]) -> None:
    """Appends elements of lst2 to lst1 thus modifying the list."""
    for element in lst2:
        lst1.append(element)
