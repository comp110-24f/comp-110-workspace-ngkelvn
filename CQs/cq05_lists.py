"""Mutating functions."""

__author__ = "730654182"


def manual_append(lst: list[int], value: int) -> None:
    """List of integers and an int value."""
    lst.append(value)  # Modifies the input list


def double(lst: list[int]) -> None:
    """Multiplies each element in list by 2."""
    i: int = 0
    while i < len(lst):
        lst[i] = lst[i] * 2  # iterating through each element.
        i += 1


# Global variables
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)  # Function call for double function.

# Print statements.
print(list_1)
print(list_2)
