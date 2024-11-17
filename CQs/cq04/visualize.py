"""Visualizing an imported function."""

__author__ = "730654182"

from CQs.cq04.concatenation import concat

from CQs.cq04.coordinates import get_coords


x = "123"  # global variable
y = "abc"

print(concat(x, y))

get_coords(x, y)  # Calls get_coords.
