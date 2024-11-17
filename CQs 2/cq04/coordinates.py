"""Printing formatted pairs of each character."""

__author__ = "730654182"


def get_coords(xs: str, ys: str) -> None:
    i = 0
    while i < len(xs):
        count = 0
        while count < len(ys):
            print(f"({xs[i]}, {ys[count]})")
            count += 1
        i += 1


get_coords("12", "34")
