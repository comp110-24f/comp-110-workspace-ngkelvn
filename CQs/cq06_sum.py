"""Summing the elements of a list using different loops."""

__author__ = "730654182"


def w_sum(vals: list[float]) -> float:
    """Takes an input of floats and returns the sum of elements."""
    total = 0.0
    index = 0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total


def f_sum(vals: list[float]) -> float:
    """Calculates sum of all elements."""
    total = 0.0
    for val in vals:
        total += val
    return total


def f_range_sum(vals: list[float]) -> float:
    """Calculates sum of all elements."""
    total = 0.0
    for i in range(len(vals)):
        total += vals[i]
    return total
